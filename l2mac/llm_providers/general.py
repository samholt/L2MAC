import asyncio
import json
import random
import re
from copy import deepcopy
from time import perf_counter, sleep

import openai
from openai import AsyncAzureOpenAI, AsyncOpenAI, AzureOpenAI, OpenAI

from l2mac.config import ApiType
from l2mac.llm_providers.openai import (
    openai_models,
    openai_rate_limits_per_tier_per_model,
)
from l2mac.llm_providers.rate_limiter import ChatRateLimiter
from l2mac.llm_providers.utils import find_best_match


def setup_chat_rate_limiter(config) -> ChatRateLimiter:
    request_limit, token_limit = setup_chat_rate_limiter_internal(config)
    return ChatRateLimiter(request_limit=request_limit, token_limit=token_limit)


def remove_nulls(d):
    return {k: v for k, v in d.items() if v is not None}


def setup_chat_rate_limiter_internal(config: dict):
    if config.llm.api_type == ApiType.azure:
        model = config.llm.model
        model_details = find_best_match(
            openai_rate_limits_per_tier_per_model[config.llm_settings.rate_limit_tier], model
        )
        request_limit = model_details["RPM"]
        token_limit = model_details["TPM"]
    elif config.llm.api_type == ApiType.openai:
        model = config.llm.model
        model_details = find_best_match(
            openai_rate_limits_per_tier_per_model[config.llm_settings.rate_limit_tier], model
        )
        request_limit = model_details["RPM"]
        token_limit = model_details["TPM"]
    else:
        raise ValueError(
            f"API type {config.llm.api_type} not yet supported, please use 'openai' or 'azure' as the API type, or contribute your own LLM API"
        )
    return request_limit, token_limit


def get_model_max_tokens(config: dict):
    if config.llm.api_type == ApiType.azure:
        model = config.llm.model
        model_details = find_best_match(openai_models, model)
        max_tokens = model_details["context_window"]
    elif config.llm.api_type == ApiType.openai:
        model = config.llm.model
        model_details = find_best_match(openai_models, model)
        max_tokens = model_details["context_window"]
    else:
        raise ValueError(
            f"API type {config.llm.api_type} not yet supported, please use 'openai' or 'azure' as the API type, or contribute your own LLM API"
        )
    return max_tokens


def get_llm_config(config, logger, name, rate_limiter):
    llm_config_dict = {
        "model": config.llm.model,
        "api_type": config.llm.api_type,
        "temperature": config.llm_settings.temperature,
        "top_p": config.llm_settings.top_p,
        "frequency_penalty": config.llm_settings.frequency_penalty,
        "presence_penalty": config.llm_settings.presence_penalty,
        "stop": config.llm_settings.stop,
        "stream": config.llm_settings.api_stream,
        "api_key": config.llm.api_key,
        "_open_ai_rate_limit_requests_per_minute": config.llm_settings.rate_limit_requests_per_minute,
        "_logger": logger,
        "_name": name,
        "_rate_limiter": rate_limiter,
        "_retry_with_exponential_backoff__initial_delay": config.llm_settings.api_retry_with_exponential_backoff__initial_delay,
        "_retry_with_exponential_backoff__exponential_base": config.llm_settings.api_retry_with_exponential_backoff__exponential_base,
        "_retry_with_exponential_backoff__jitter": config.llm_settings.api_retry_with_exponential_backoff__jitter,
        "_retry_with_exponential_backoff__max_retries": config.llm_settings.api_retry_with_exponential_backoff__max_retries,
    }
    if config.llm.api_type == ApiType.azure:
        llm_config_dict.update({"azure_endpoint": config.llm.base_url, "api_version": config.llm.api_version})
    return deepcopy(llm_config_dict)


def chat_completion_rl(**kwargs):
    # Implements retry_with_exponential_backoff
    initial_delay = kwargs.get("_retry_with_exponential_backoff__initial_delay", 1)
    exponential_base = kwargs.get("_retry_with_exponential_backoff__exponential_base", 2)
    jitter = kwargs.get("_retry_with_exponential_backoff__jitter", True)
    max_retries = kwargs.get("_retry_with_exponential_backoff__max_retries", 10)
    stream = kwargs.get("stream", False)

    kwargs.pop("_retry_with_exponential_backoff__initial_delay", None)
    kwargs.pop("_retry_with_exponential_backoff__exponential_base", None)
    kwargs.pop("_retry_with_exponential_backoff__jitter", None)
    kwargs.pop("_retry_with_exponential_backoff__max_retries", None)

    logger = kwargs.get("_logger", None)
    name = kwargs.get("_name", None)
    if kwargs.get("config", None) and kwargs.get("config", None).llm.api_type == "azure":
        use_azure_api = True
    else:
        use_azure_api = False

    errors: tuple = (openai.RateLimitError, openai.APIError, openai.APITimeoutError, openai.APIConnectionError)

    # Initialize variables
    num_retries = 0
    delay = initial_delay

    # Loop until a successful response or max_retries is hit or an exception is raised
    while True:
        try:
            if stream:
                return asyncio.run(async_chat_completion_rl_inner(**kwargs))
            else:
                return chat_completion_rl_inner(**kwargs)

        # Retry on specified errors
        except errors as e:
            # Increment retries
            if logger:
                logger.info(
                    f"[{name}][OpenAI API Request Error] {type(e)} {e.args} | num_retries: {num_retries} / {max_retries}"
                )
            else:
                print(
                    f"[{name}][OpenAI API Request Error] {type(e)} {e.args} | num_retries: {num_retries} / {max_retries}"
                )
            num_retries += 1

            # Check if max retries has been reached
            if num_retries > max_retries:
                if logger:
                    logger.info(
                        f"[{name}][OpenAI API Request Error] Exception Maximum number of retries ({max_retries}) exceeded. | num_retries: {num_retries} / {max_retries}"
                    )
                else:
                    print(
                        f"[{name}][OpenAI API Request Error] Exception Maximum number of retries ({max_retries}) exceeded. | num_retries: {num_retries} / {max_retries}"
                    )
                raise Exception(f"Maximum number of retries ({max_retries}) exceeded.")

            # Increment the delay
            delay *= exponential_base * (1 + jitter * random.random())

            # Sleep for the delay
            if use_azure_api:
                match = re.search(r"Please retry after (\d+) seconds", e.args[0])
                if match:
                    delay = int(match.group(1))
                    # delay = int(match.group(1))
            if logger:
                logger.info(
                    f"[{name}][OpenAI API Request Error] {type(e)} {e.args} | num_retries: {num_retries} / {max_retries} | Now sleeping for {delay} seconds"
                )
            else:
                print(
                    f"[{name}][OpenAI API Request Error] {type(e)} {e.args} | num_retries: {num_retries} / {max_retries} | Now sleeping for {delay} seconds"
                )
            # sleep(delay // 2.0)
            if delay > 60:
                delay = 60
            sleep(delay)

        # Raise exceptions for any errors not specified
        except Exception as e:
            raise e


async def async_chat_completion_rl_inner(**kwargs):
    kwargs.get("_logger", None)
    kwargs.get("_name", None)
    rate_limiter = kwargs.get("_rate_limiter", None)
    api_type = kwargs.get("api_type", ApiType.openai)
    if api_type == ApiType.openai:
        aclient = AsyncOpenAI(api_key=kwargs["api_key"])
    elif api_type == ApiType.azure:
        aclient = AsyncAzureOpenAI(
            api_key=kwargs["api_key"], api_version=kwargs["api_version"], azure_endpoint=kwargs["azure_endpoint"]
        )
    keys_to_remove = {
        "_open_ai_rate_limit_requests_per_minute",
        "_logger",
        "_name",
        "api_key",
        "api_version",
        "azure_endpoint",
        "_rate_limiter",
        "stream",
        "api_type",
    }
    kwargs = {k: v for k, v in kwargs.items() if k not in keys_to_remove}
    perf_counter()
    # if logger:
    #     logger.info(f"[{name}][OpenAI API Request] {kwargs}")
    # pretty_print_chat_messages(kwargs['messages'])

    if rate_limiter:
        rate_limiter.consume(**kwargs)
        responses = await aclient.chat.completions.create(**kwargs)
    else:
        responses = await aclient.chat.completions.create(**kwargs)
    response = {}
    chunks = []
    async for chunk in responses:
        print(chunk)
        if "choices" not in chunk or len(chunk["choices"]) == 0:
            continue
        chunk_message = chunk["choices"][0]["delta"].to_dict_recursive()  # extract the message
        chunks.append(chunk_message)
        print(chunk_message)
        for k, v in chunk_message.items():
            if k in response:
                if isinstance(response[k], dict):
                    for k2, v2 in v.items():
                        if k2 in response[k]:
                            response[k][k2] += v2
                        else:
                            response[k][k2] = v2
                else:
                    response[k] += v
            else:
                response[k] = v
    print(response)
    return_response = {"choices": [{"message": response}]}
    # if logger:
    # logger.info(f"[{name}][OpenAI API Returned] Elapsed request time: {perf_counter() - t0}s | response: {response}")
    return return_response


def chat_completion_rl_inner(**kwargs):
    kwargs.get("_logger", None)
    kwargs.get("_name", None)
    rate_limiter = kwargs.get("_rate_limiter", None)
    api_type = kwargs.get("api_type", ApiType.openai)
    if api_type == ApiType.openai:
        client = OpenAI(api_key=kwargs["api_key"])
    elif api_type == ApiType.azure:
        client = AzureOpenAI(
            api_key=kwargs["api_key"], api_version=kwargs["api_version"], azure_endpoint=kwargs["azure_endpoint"]
        )
    keys_to_remove = {
        "_open_ai_rate_limit_requests_per_minute",
        "_logger",
        "_name",
        "api_key",
        "api_version",
        "azure_endpoint",
        "_rate_limiter",
        "stream",
        "api_type",
    }
    kwargs = {k: v for k, v in kwargs.items() if k not in keys_to_remove}
    perf_counter()
    # if logger:
    #     logger.info(f"[{name}][OpenAI API Request] {kwargs}")
    # pretty_print_chat_messages(kwargs['messages'])
    if rate_limiter:
        rate_limiter.consume(**kwargs)
        response = client.chat.completions.create(**kwargs)
    else:
        response = client.chat.completions.create(**kwargs)
    # if logger:
    # logger.info(f"[{name}][OpenAI API Returned] Elapsed request time: {perf_counter() - t0}s | response: {response}")
    response = json.loads(
        response.model_dump_json(), object_hook=remove_nulls
    )  # Convert to dict, easier to save as a replay buffer for debugging
    # OpenAI-API expects none objects to be removed
    return response
