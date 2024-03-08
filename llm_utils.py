# imports
import random
import time
import openai
import os
import re
from copy import deepcopy
import tiktoken
import asyncio
# from openai.embeddings_utils import get_embedding, cosine_similarity

# Tokenizer
CL100K_ENCODER = tiktoken.get_encoding("cl100k_base")
P50K_ENCODER = tiktoken.get_encoding("p50k_base")

AZURE_SOUTH_ENDPOINT = "https://vdslabazuremloai-uksouth.openai.azure.com/"
AZURE_MAIN_ENDPOINT = "https://vdslabazuremloai.openai.azure.com/"
AZURE_OPENAI_KEY_SOUTH = os.getenv("AZURE_OPENAI_KEY_SOUTH")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")

AZURE_SWISS_ENDPOINT = "https://vdslabten-oai-swnorth.openai.azure.com/"
AZURE_NEW_UK_SOUTH_ENDPOINT = ""
KEY_SWISS = os.getenv("AZURE_OPENAI_KEY_SWISS")
KEY_NEW_UK_SOUTH = os.getenv("AZURE_OPENAI_KEY_NEWUKSOUTH")


AZURE_MODEL_DETAILS_MAP = {"gpt-3.5-turbo": {'engine': "gpt35turbo0613_20230925",
                                             'api_key': os.getenv("AZURE_OPENAI_KEY_SOUTH"),
                                             'api_version': "2023-07-01-preview",
                                             'api_base': AZURE_SOUTH_ENDPOINT,
                                             'api_type': "azure",
                                             'properties': {'model_name': 'gpt-35-turbo',
                                                            'model_version': '0613',
                                                            'version_update_policy': 'Once the current version expires.',
                                                            'deployment_type': 'Standard',
                                                            'content_filter': 'Default',
                                                            'tokens_per_minute_rate_limit_(thousands)': 80,
                                                            'rate_limit_(Tokens per minute)': 80000,
                                                            'rate_limit_(Requests per minute)': 480,
                                                            'max_tokens': 4097
                                             }},
                            "gpt-3.5-turbo-16k": {'engine': "gpt35turbo-16k_20230904",
                                             'api_key': os.getenv("AZURE_OPENAI_KEY_SOUTH"),
                                             'api_version': "2023-07-01-preview",
                                             'api_base': AZURE_SOUTH_ENDPOINT,
                                             'api_type': "azure",
                                             'properties': {'model_name': 'gpt-35-turbo-16k',
                                                            'model_version': '0613',
                                                            'version_update_policy': 'Once a new default version is available.',
                                                            'deployment_type': 'Standard',
                                                            'content_filter': 'Default',
                                                            'tokens_per_minute_rate_limit_(thousands)': 120,
                                                            'rate_limit_(Tokens per minute)': 120000,
                                                            'rate_limit_(Requests per minute)': 720,
                                                            'max_tokens': 16385
                                             }},
                            "gpt-3.5-turbo-old": {'engine': "gpt35turbo_20230727",
                                             'api_key': os.getenv("AZURE_OPENAI_KEY"),
                                             'api_version': "2023-07-01-preview",
                                             'api_base': AZURE_MAIN_ENDPOINT,
                                             'api_type': "azure",
                                             'properties': {'model_name': 'gpt-35-turbo',
                                                            'model_version': '0301',
                                                            'deployment_type': 'Standard',
                                                            'content_filter': 'Default',
                                                            'tokens_per_minute_rate_limit_(thousands)': 120,
                                                            'rate_limit_(Tokens per minute)': 120000,
                                                            'rate_limit_(Requests per minute)': 720,
                                                            'max_tokens': 4097
                                             }},
                            "gpt-3.5-turbo-2": {'engine': "gpt35turbo_20230818",
                                             'api_key': os.getenv("AZURE_OPENAI_KEY"),
                                             'api_version': "2023-07-01-preview",
                                             'api_base': AZURE_MAIN_ENDPOINT,
                                             'api_type': "azure",
                                             'properties': {'model_name': 'gpt-35-turbo',
                                                            'model_version': '0301',
                                                            'version_update_policy': 'Once a new default version is available.',
                                                            'deployment_type': 'Standard',
                                                            'content_filter': 'Default',
                                                            'tokens_per_minute_rate_limit_(thousands)': 120,
                                                            'rate_limit_(Tokens per minute)': 120000,
                                                            'rate_limit_(Requests per minute)': 720,
                                                            'max_tokens': 4097
                                             }},
                            "text-embedding-ada-002": {'engine': "embAda002_20230727",
                                             'api_key': os.getenv("AZURE_OPENAI_KEY"),
                                             'api_version': "2023-07-01-preview",
                                             'api_base': AZURE_MAIN_ENDPOINT,
                                             'api_type': "azure",
                                             'properties': {
                                                 'model_name': 'text-embedding-ada-002',
                                                 'model_version': '2',
                                                 'version_update_policy': 'Once a new default version is available.',
                                                 'deployment_type': 'Standard',
                                                 'content_filter': 'Default',
                                                 'tokens_per_minute_rate_limit_(thousands)': 120,
                                                 'rate_limit_(Tokens per minute)': 120000,
                                                 'rate_limit_(Requests per minute)': 720,
                                                 'max_tokens': 8191,
                                                 'max_batch_size': 16, # 2048 Should be, microsoft says 16 at this time
                                             },},
                            "gpt-4":        {'engine': "gpt4_20230815",
                                             'api_key': os.getenv("AZURE_OPENAI_KEY_SOUTH"),
                                             'api_version': "2023-07-01-preview",
                                             'api_base': AZURE_SOUTH_ENDPOINT,
                                             'api_type': "azure",
                                             'properties': {
                                                 'model_name': 'gpt-4',
                                                 'model_version': '0613',
                                                 'version_update_policy': 'Once a new default version is available.',
                                                 'deployment_type': 'Standard',
                                                 'content_filter': 'Default',
                                                 'tokens_per_minute_rate_limit_(thousands)': 10,
                                                 'rate_limit_(Tokens per minute)': 10000,
                                                 'rate_limit_(Requests per minute)': 60,
                                                 'max_tokens': 8192
                                             }}, # OLD GPT-4
                            "gpt-4-0":        {'engine': "SWNorth-gpt-4-0613-20231016-4",
                                             'api_key': KEY_SWISS,
                                             'api_version': "2023-07-01-preview",
                                             'api_base': AZURE_SWISS_ENDPOINT,
                                             'api_type': "azure",
                                             'properties': {
                                                 'model_name': 'gpt-4',
                                                 'model_version': '0613',
                                                 'version_update_policy': 'Once a new default version is available.',
                                                 'deployment_type': 'Standard',
                                                 'content_filter': 'Default',
                                                 'tokens_per_minute_rate_limit_(thousands)': 10,
                                                 'rate_limit_(Tokens per minute)': 10000,
                                                 'rate_limit_(Requests per minute)': 60,
                                                 'max_tokens': 8192
                                             }},
                            "gpt-4-1":        {'engine': "SWNorth-gpt-4-0613-20231016-3",
                                             'api_key': KEY_SWISS,
                                             'api_version': "2023-07-01-preview",
                                             'api_base': AZURE_SWISS_ENDPOINT,
                                             'api_type': "azure",
                                             'properties': {
                                                 'model_name': 'gpt-4',
                                                 'model_version': '0613',
                                                 'version_update_policy': 'Once a new default version is available.',
                                                 'deployment_type': 'Standard',
                                                 'content_filter': 'Default',
                                                 'tokens_per_minute_rate_limit_(thousands)': 10,
                                                 'rate_limit_(Tokens per minute)': 10000,
                                                 'rate_limit_(Requests per minute)': 60,
                                                 'max_tokens': 8192
                                             }},
                            "gpt-4-2":        {'engine': "SWNorth-gpt-4-0613-20231016-2",
                                             'api_key': KEY_SWISS,
                                             'api_version': "2023-07-01-preview",
                                             'api_base': AZURE_SWISS_ENDPOINT,
                                             'api_type': "azure",
                                             'properties': {
                                                 'model_name': 'gpt-4',
                                                 'model_version': '0613',
                                                 'version_update_policy': 'Once a new default version is available.',
                                                 'deployment_type': 'Standard',
                                                 'content_filter': 'Default',
                                                 'tokens_per_minute_rate_limit_(thousands)': 10,
                                                 'rate_limit_(Tokens per minute)': 10000,
                                                 'rate_limit_(Requests per minute)': 60,
                                                 'max_tokens': 8192
                                             }},
                            "gpt-4-3":        {'engine': "SWNorth-gpt-4-0613-20231016",
                                             'api_key': KEY_SWISS,
                                             'api_version': "2023-07-01-preview",
                                             'api_base': AZURE_SWISS_ENDPOINT,
                                             'api_type': "azure",
                                             'properties': {
                                                 'model_name': 'gpt-4',
                                                 'model_version': '0613',
                                                 'version_update_policy': 'Once a new default version is available.',
                                                 'deployment_type': 'Standard',
                                                 'content_filter': 'Default',
                                                 'tokens_per_minute_rate_limit_(thousands)': 10,
                                                 'rate_limit_(Tokens per minute)': 10000,
                                                 'rate_limit_(Requests per minute)': 60,
                                                 'max_tokens': 8192
                                             }},
                            "gpt-4-32k-0":   {'engine': "SWNorth-gpt-4-32k-0613-20231016-4",
                                             'api_key': KEY_SWISS,
                                             'api_version': "2023-07-01-preview",
                                             'api_base': AZURE_SWISS_ENDPOINT,
                                             'api_type': "azure",
                                             'properties': {
                                                 'model_name': 'gpt-4-32k',
                                                 'model_version': '0613',
                                                 'version_update_policy': 'Once a new default version is available.',
                                                 'deployment_type': 'Standard',
                                                 'content_filter': 'Default',
                                                 'tokens_per_minute_rate_limit_(thousands)': 20,
                                                 'rate_limit_(Tokens per minute)': 20000,
                                                 'rate_limit_(Requests per minute)': 120,
                                                 'max_tokens': 32768
                                             }},
                            "gpt-4-32k-1":   {'engine': "SWNorth-gpt-4-32k-0613-20231016-3",
                                             'api_key': KEY_SWISS,
                                             'api_version': "2023-07-01-preview",
                                             'api_base': AZURE_SWISS_ENDPOINT,
                                             'api_type': "azure",
                                             'properties': {
                                                 'model_name': 'gpt-4-32k',
                                                 'model_version': '0613',
                                                 'version_update_policy': 'Once a new default version is available.',
                                                 'deployment_type': 'Standard',
                                                 'content_filter': 'Default',
                                                 'tokens_per_minute_rate_limit_(thousands)': 20,
                                                 'rate_limit_(Tokens per minute)': 20000,
                                                 'rate_limit_(Requests per minute)': 120,
                                                 'max_tokens': 32768
                                             }},
                            "gpt-4-32k-2":   {'engine': "SWNorth-gpt-4-32k-0613-20231016-2",
                                             'api_key': KEY_SWISS,
                                             'api_version': "2023-07-01-preview",
                                             'api_base': AZURE_SWISS_ENDPOINT,
                                             'api_type': "azure",
                                             'properties': {
                                                 'model_name': 'gpt-4-32k',
                                                 'model_version': '0613',
                                                 'version_update_policy': 'Once a new default version is available.',
                                                 'deployment_type': 'Standard',
                                                 'content_filter': 'Default',
                                                 'tokens_per_minute_rate_limit_(thousands)': 20,
                                                 'rate_limit_(Tokens per minute)': 20000,
                                                 'rate_limit_(Requests per minute)': 120,
                                                 'max_tokens': 32768
                                             }},
                            "gpt-4-32k-3":   {'engine': "SWNorth-gpt-4-32k-0613-20231016",
                                             'api_key': KEY_SWISS,
                                             'api_version': "2023-07-01-preview",
                                             'api_base': AZURE_SWISS_ENDPOINT,
                                             'api_type': "azure",
                                             'properties': {
                                                 'model_name': 'gpt-4-32k',
                                                 'model_version': '0613',
                                                 'version_update_policy': 'Once a new default version is available.',
                                                 'deployment_type': 'Standard',
                                                 'content_filter': 'Default',
                                                 'tokens_per_minute_rate_limit_(thousands)': 20,
                                                 'rate_limit_(Tokens per minute)': 20000,
                                                 'rate_limit_(Requests per minute)': 120,
                                                 'max_tokens': 32768
                                             }},
                            "gpt-35-turbo-16k-0":   {'engine': "SWNorth-gpt-35-turbo-16k-0613-20231016-5",
                                             'api_key': KEY_SWISS,
                                             'api_version': "2023-07-01-preview",
                                             'api_base': AZURE_SWISS_ENDPOINT,
                                             'api_type': "azure",
                                             'properties': {
                                                 'model_name': 'gpt-35-turbo-16k',
                                                 'model_version': '0613',
                                                 'version_update_policy': 'Once a new default version is available.',
                                                 'deployment_type': 'Standard',
                                                 'content_filter': 'Default',
                                                 'tokens_per_minute_rate_limit_(thousands)': 60,
                                                 'rate_limit_(Tokens per minute)': 60000,
                                                 'rate_limit_(Requests per minute)': 360,
                                                 'max_tokens': 16385
                                             }},
                            # "gpt-3-16k-misslabelled":    {'engine': "gpt4-32k_20230815",
                            #                  'api_key': os.getenv("AZURE_OPENAI_KEY_SOUTH"),
                            #                  'api_version': "2023-07-01-preview",
                            #                  'api_base': AZURE_SOUTH_ENDPOINT,
                            #                  'api_type': "azure",
                            #                  'properties': {
                            #                      'model_name': 'gpt-35-turbo-16k',
                            #                      'model_version': '0613',
                            #                      'version_update_policy': 'Once a new default version is available.',
                            #                      'deployment_type': 'Standard',
                            #                      'content_filter': 'Default',
                            #                      'tokens_per_minute_rate_limit_(thousands)': 120,
                            #                      'rate_limit_(Tokens per minute)': 120000,
                            #                      'rate_limit_(Requests per minute)': 720,
                            #                      'max_tokens': 16385
                            #                     }}
                            "gpt-4-32k":    {'engine': "gpt4-32k_20230830",
                                             'api_key': os.getenv("AZURE_OPENAI_KEY_SOUTH"),
                                             'api_version': "2023-07-01-preview",
                                             'api_base': AZURE_SOUTH_ENDPOINT,
                                             'api_type': "azure",
                                             'properties': {
                                                 'model_name': 'gpt-4-32k',
                                                 'model_version': '0613',
                                                 'version_update_policy': 'Once a new default version is available.',
                                                 'deployment_type': 'Standard',
                                                 'content_filter': 'Default',
                                                 'tokens_per_minute_rate_limit_(thousands)': 30,
                                                 'rate_limit_(Tokens per minute)': 30000,
                                                 'rate_limit_(Requests per minute)': 180,
                                                 'max_tokens': 32768
                                                }}
                            }

OPENAI_MODEL_DETAILS_MAP = {
    'default': {
        'tpm': 250000,
        'rpm': 3000
    },
    'gpt-3.5-turbo': {
        'tpm': 90000,
        'rpm': 3500,
        'max_tokens': 4097
    },
    'gpt-3.5-turbo-0301': {
        'tpm': 90000,
        'rpm': 3500,
        'max_tokens': 4097
    },
    'gpt-3.5-turbo-0613': {
        'tpm': 90000,
        'rpm': 3500,
        'max_tokens': 4097
    },
    'gpt-3.5-turbo-16k': {
        'tpm': 180000,
        'rpm': 3500,
        'max_tokens': 16385 
    },
    'gpt-3.5-turbo-16k-0613': {
        'tpm': 180000,
        'rpm': 3500,
        'max_tokens': 16385
    },
    'gpt-4': {
        'tpm': 40000,
        'rpm': 200,
        'max_tokens': 8192
    },
    'gpt-4-0314': {
        'tpm': 40000,
        'rpm': 200,
        'max_tokens': 8192
    },
    'gpt-4-0613': {
        'tpm': 40000,
        'rpm': 200,
        'max_tokens': 8192
    }
}

def get_llm_config(config, logger, name, rate_limiter):
    return deepcopy({'model': config.run.model,
            'temperature': config.run.temperature,
            'top_p': config.run.top_p,
            'frequency_penalty': config.run.frequency_penalty,
            'presence_penalty': config.run.presence_penalty,
            'stop': config.run.stop,
            'request_timeout': config.setup.api_request_timeout,
            'stream': config.setup.api_stream,
            '_open_ai_rate_limit_requests_per_minute': config.setup.open_ai_rate_limit_requests_per_minute,
            '_use_azure_api': config.setup.use_azure_api,
            '_logger': logger,
            '_name': name,
            '_rate_limiter': rate_limiter,
            '_retry_with_exponential_backoff__initial_delay': config.setup.api_retry_with_exponential_backoff__initial_delay,
            '_retry_with_exponential_backoff__exponential_base': config.setup.api_retry_with_exponential_backoff__exponential_base,
            '_retry_with_exponential_backoff__jitter': config.setup.api_retry_with_exponential_backoff__jitter,
            '_retry_with_exponential_backoff__max_retries': config.setup.api_retry_with_exponential_backoff__max_retries})

def setup_chat_rate_limiter(config: dict):
    if config.setup.use_azure_api:
        model = config.run.model
        model_details = AZURE_MODEL_DETAILS_MAP[model]
        request_limit = model_details['properties']['rate_limit_(Requests per minute)']
        token_limit = model_details['properties']['rate_limit_(Tokens per minute)']
    else:
        model = config.run.model
        model_details = OPENAI_MODEL_DETAILS_MAP[model]
        request_limit = model_details['rpm']
        token_limit = model_details['tpm']
    return request_limit, token_limit

def get_model_max_tokens(config: dict):
    if config.setup.use_azure_api:
        model = config.run.model
        model_details = AZURE_MODEL_DETAILS_MAP[model]
        max_tokens = model_details['properties']['max_tokens']
    else:
        model = config.run.model
        model_details = OPENAI_MODEL_DETAILS_MAP[model]
        max_tokens = model_details['properties']['max_tokens']
    return max_tokens

def pretty_print_chat_messages(messages, num_tokens=None, max_tokens=None, logger=None, response_msg=False, step_idx=None, total_steps=None, max_re_tries=None, re_tries=None):
    COLORS = {
        "system": "\033[95m",      # Light Magenta
        "user": "\033[94m",       # Light Blue
        "assistant": "\033[92m",   # Light Green
        "tokens": "\033[91m"   # Light Red
    }

    if response_msg:
        print("[LLM RESPONSE MESSAGE]")  # Reset color at the end
        if logger:
            logger.info("[LLM RESPONSE MESSAGE]")
    
    for msg in messages:
        role = msg['role']
        color = COLORS.get(role, COLORS["system"])  # Default to system color if role not found
        formatted_role = role.capitalize()
        content = msg['content']
        if role == "assistant" and 'function_call' in msg:
            formatted_role = "Function Call"
            print(f"{color}[{formatted_role}] [{msg['function_call']['name']}] {msg['function_call']['arguments']}\033[0m")  # Reset color at the end
            if logger:
                logger.info(f"[{formatted_role}] [{msg['function_call']['name']}] {msg['function_call']['arguments']}")
        else:
            print(f"{color}[{formatted_role}] {content}\033[0m")  # Reset color at the end
            if logger:
                logger.info(f"[{formatted_role}] {content}")

    if not response_msg:
        if step_idx is not None and total_steps is not None:
            if num_tokens and max_tokens:
                if max_re_tries is not None and re_tries is not None:
                    print(f"{COLORS['tokens']}[Progress: Step {step_idx + 1}/{total_steps} | Retries: {re_tries}/{max_re_tries} | Token Capacity Used: {((num_tokens / max_tokens) * 100.0):.2f}% | Tokens remaining {max_tokens - num_tokens}]\033[0m")
                    if logger:
                        logger.info(f"[Progress: Step {step_idx + 1}/{total_steps} | Retries: {re_tries}/{max_re_tries} | Token Capacity Used: {((num_tokens / max_tokens) * 100.0):.2f}% | Tokens remaining {max_tokens - num_tokens}]")
                else:
                    print(f"{COLORS['tokens']}[Progress: Step {step_idx + 1}/{total_steps} | Token Capacity Used: {((num_tokens / max_tokens) * 100.0):.2f}% | Tokens remaining {max_tokens - num_tokens}]\033[0m")
                    if logger:
                        logger.info(f"[Progress: Step {step_idx + 1}/{total_steps} | Token Capacity Used: {((num_tokens / max_tokens) * 100.0):.2f}% | Tokens remaining {max_tokens - num_tokens}]")
                    
        else:
            if num_tokens and max_tokens:
                print(f"{COLORS['tokens']}[Token Capacity Used: {((num_tokens / max_tokens) * 100.0):.2f}% | Tokens remaining {max_tokens - num_tokens}]\033[0m")
                if logger:
                    logger.info(f"[Token Capacity Used: {((num_tokens / max_tokens) * 100.0):.2f}% | Tokens remaining {max_tokens - num_tokens}]")



def chat_completion_rl(**kwargs):
    # Implements retry_with_exponential_backoff
    initial_delay = kwargs.get('_retry_with_exponential_backoff__initial_delay', 1)
    exponential_base = kwargs.get('_retry_with_exponential_backoff__exponential_base', 2)
    jitter = kwargs.get('_retry_with_exponential_backoff__jitter', True)
    max_retries = kwargs.get('_retry_with_exponential_backoff__max_retries', 10)
    use_azure_api = kwargs.get('_use_azure_api', True)
    stream = kwargs.get('stream', False)

    kwargs.pop('_retry_with_exponential_backoff__initial_delay', None)
    kwargs.pop('_retry_with_exponential_backoff__exponential_base', None)
    kwargs.pop('_retry_with_exponential_backoff__jitter', None)
    kwargs.pop('_retry_with_exponential_backoff__max_retries', None)
    kwargs.pop('_use_azure_api', None)

    logger = kwargs.get('_logger', None)
    name = kwargs.get('_name', None)

    errors: tuple = (openai.error.RateLimitError,openai.error.APIError,openai.error.Timeout)

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
                logger.info(f"[{name}][OpenAI API Request Error] {type(e)} {e.args} | num_retries: {num_retries} / {max_retries}")
            else:
                print(f"[{name}][OpenAI API Request Error] {type(e)} {e.args} | num_retries: {num_retries} / {max_retries}")
            num_retries += 1

            # Check if max retries has been reached
            if num_retries > max_retries:
                if logger:
                    logger.info(f"[{name}][OpenAI API Request Error] Exception Maximum number of retries ({max_retries}) exceeded. | num_retries: {num_retries} / {max_retries}")
                else:
                    print(f"[{name}][OpenAI API Request Error] Exception Maximum number of retries ({max_retries}) exceeded. | num_retries: {num_retries} / {max_retries}")
                raise Exception(
                    f"Maximum number of retries ({max_retries}) exceeded."
                )

            # Increment the delay
            delay *= exponential_base * (1 + jitter * random.random())

            # Sleep for the delay
            if use_azure_api:
                match = re.search(r'Please retry after (\d+) seconds', e.args[0])
                if match:
                    delay = int(match.group(1))
                    # delay = int(match.group(1))
            if logger:
                logger.info(f"[{name}][OpenAI API Request Error] {type(e)} {e.args} | num_retries: {num_retries} / {max_retries} | Now sleeping for {delay} seconds")
            else:
                print(f"[{name}][OpenAI API Request Error] {type(e)} {e.args} | num_retries: {num_retries} / {max_retries} | Now sleeping for {delay} seconds")
            # time.sleep(delay // 2.0)
            if delay > 60:
                delay = 60
            time.sleep(delay)

        # Raise exceptions for any errors not specified
        except Exception as e:
            raise e

async def async_chat_completion_rl_inner(**kwargs):
    logger = kwargs.get('_logger', None)
    name = kwargs.get('_name', None)
    use_azure_api = kwargs.get('_use_azure_api', True)
    rate_limiter = kwargs.get('_rate_limiter', None)
    model = kwargs.get('model', 'gpt-3.5-turbo')
    if use_azure_api:
        model_details = AZURE_MODEL_DETAILS_MAP[model]
        kwargs.pop('model', None)
        kwargs['engine'] = model_details['engine']
        kwargs['api_key'] = model_details['api_key']
        kwargs['api_version'] = model_details['api_version']
        kwargs['api_base'] = model_details['api_base']
        kwargs['api_type'] = model_details['api_type']
        kwargs.pop('_open_ai_rate_limit_requests_per_minute', None)
        kwargs['_open_ai_rate_limit_requests_per_minute'] = model_details['properties']['rate_limit_(Requests per minute)']

    # requests_per_minute = kwargs.get('_open_ai_rate_limit_requests_per_minute', 3000)
    # delay_in_seconds = 60.0 / requests_per_minute
    # time.sleep(delay_in_seconds)

    kwargs.pop('_open_ai_rate_limit_requests_per_minute', None)
    kwargs.pop('_logger', None)
    kwargs.pop('_name', None)
    kwargs.pop('_rate_limiter', None)
    kwargs.pop('_rate_limiter', None)
    t0 = time.perf_counter()
    # if logger:
    #     logger.info(f"[{name}][OpenAI API Request] {kwargs}")
    # pretty_print_chat_messages(kwargs['messages'])

    if rate_limiter:
        rate_limiter.consume(**kwargs)
        responses = await openai.ChatCompletion.acreate(**kwargs)
    else:
        responses = await openai.ChatCompletion.acreate(**kwargs)
    response = {}
    chunks = []
    async for chunk in responses:
        print(chunk)
        if 'choices' not in chunk or len(chunk['choices']) == 0:
            continue
        chunk_message = chunk['choices'][0]['delta'].to_dict_recursive()  # extract the message
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
        # logger.info(f"[{name}][OpenAI API Returned] Elapsed request time: {time.perf_counter() - t0}s | response: {response}")
    return return_response

def chat_completion_rl_inner(**kwargs):
    logger = kwargs.get('_logger', None)
    name = kwargs.get('_name', None)
    use_azure_api = kwargs.get('_use_azure_api', True)
    rate_limiter = kwargs.get('_rate_limiter', None)
    model = kwargs.get('model', 'gpt-3.5-turbo')
    if use_azure_api:
        model_details = AZURE_MODEL_DETAILS_MAP[model]
        kwargs.pop('model', None)
        kwargs['engine'] = model_details['engine']
        kwargs['api_key'] = model_details['api_key']
        kwargs['api_version'] = model_details['api_version']
        kwargs['api_base'] = model_details['api_base']
        kwargs['api_type'] = model_details['api_type']
        kwargs.pop('_open_ai_rate_limit_requests_per_minute', None)
        kwargs['_open_ai_rate_limit_requests_per_minute'] = model_details['properties']['rate_limit_(Requests per minute)']

    # requests_per_minute = kwargs.get('_open_ai_rate_limit_requests_per_minute', 3000)
    # delay_in_seconds = 60.0 / requests_per_minute
    # time.sleep(delay_in_seconds)

    kwargs.pop('_open_ai_rate_limit_requests_per_minute', None)
    kwargs.pop('_logger', None)
    kwargs.pop('_name', None)
    kwargs.pop('_rate_limiter', None)
    kwargs.pop('_rate_limiter', None)
    kwargs.pop('stream', None)
    t0 = time.perf_counter()
    # if logger:
    #     logger.info(f"[{name}][OpenAI API Request] {kwargs}")
    # pretty_print_chat_messages(kwargs['messages'])

    if rate_limiter:
        rate_limiter.consume(**kwargs)
        response = openai.ChatCompletion.create(**kwargs)
    else:
        response = openai.ChatCompletion.create(**kwargs)
    # if logger:
        # logger.info(f"[{name}][OpenAI API Returned] Elapsed request time: {time.perf_counter() - t0}s | response: {response}")
    return response

# =================================================================================================
# Embedding

def replace_newlines(input_data):
    if isinstance(input_data, str):
        return input_data.replace("\n", " ")
    elif isinstance(input_data, list):
        return [item.replace("\n", " ") for item in input_data]
    else:
        raise ValueError("Input should be either a string or a list of strings")

# Unit tests
def test_replace_newlines():
    assert replace_newlines("Hello\nWorld") == "Hello World"
    assert replace_newlines(["Hello\nWorld", "Python\nRocks"]) == ["Hello World", "Python Rocks"]
    assert replace_newlines("No newline here") == "No newline here"
    assert replace_newlines(["No newline here", "Neither here"]) == ["No newline here", "Neither here"]
    assert replace_newlines("\n\n") == "  "
    assert replace_newlines(["\n", "\n\n"]) == [" ", "  "]
    print("All tests passed!")


def embedding_rl(input, **kwargs):
    # Implements retry_with_exponential_backoff
    initial_delay = kwargs.get('_retry_with_exponential_backoff__initial_delay', 1)
    exponential_base = kwargs.get('_retry_with_exponential_backoff__exponential_base', 2)
    jitter = kwargs.get('_retry_with_exponential_backoff__jitter', True)
    max_retries = kwargs.get('_retry_with_exponential_backoff__max_retries', 10)
    use_azure_api = kwargs.get('_use_azure_api', True)

    kwargs.pop('_retry_with_exponential_backoff__initial_delay', None)
    kwargs.pop('_retry_with_exponential_backoff__exponential_base', None)
    kwargs.pop('_retry_with_exponential_backoff__jitter', None)
    kwargs.pop('_retry_with_exponential_backoff__max_retries', None)
    kwargs.pop('_use_azure_api', None)

    logger = kwargs.get('_logger', None)
    name = kwargs.get('_name', None)

    errors: tuple = (openai.error.RateLimitError,)

    # Initialize variables
    num_retries = 0
    delay = initial_delay

    # Loop until a successful response or max_retries is hit or an exception is raised
    while True:
        try:
            return embedding_rl_inner(input, **kwargs)

        # Retry on specified errors
        except errors as e:
            # Increment retries
            if logger:
                logger.info(f"[{name}][OpenAI API Request Error] {type(e)} {e.args} | num_retries: {num_retries} / {max_retries}")
            else:
                print(f"[{name}][OpenAI API Request Error] {type(e)} {e.args} | num_retries: {num_retries} / {max_retries}")
            num_retries += 1

            # Check if max retries has been reached
            if num_retries > max_retries:
                if logger:
                    logger.info(f"[{name}][OpenAI API Request Error] Exception Maximum number of retries ({max_retries}) exceeded. | num_retries: {num_retries} / {max_retries}")
                else:
                    print(f"[{name}][OpenAI API Request Error] Exception Maximum number of retries ({max_retries}) exceeded. | num_retries: {num_retries} / {max_retries}")
                raise Exception(
                    f"Maximum number of retries ({max_retries}) exceeded."
                )

            # Increment the delay
            delay *= exponential_base * (1 + jitter * random.random())

            # Sleep for the delay
            if use_azure_api:
                match = re.search(r'Please retry after (\d+) seconds', e.args[0])
                if match:
                    delay = int(match.group(1)) + 1.5
                    # delay = int(match.group(1))
            if logger:
                logger.info(f"[{name}][OpenAI API Request Error] {type(e)} {e.args} | num_retries: {num_retries} / {max_retries} | Now sleeping for {delay} seconds")
            else:
                print(f"[{name}][OpenAI API Request Error] {type(e)} {e.args} | num_retries: {num_retries} / {max_retries} | Now sleeping for {delay} seconds")
            time.sleep(delay // 2.0)

        # Raise exceptions for any errors not specified
        except Exception as e:
            raise e

def embedding_rl_inner(input, **kwargs):
    logger = kwargs.get('_logger', None)
    name = kwargs.get('_name', None)
    use_azure_api = kwargs.get('_use_azure_api', True)
    rate_limiter = kwargs.get('_rate_limiter', None)
    model = kwargs.get('model', 'text-embedding-ada-002')
    if use_azure_api:
        model_details = AZURE_MODEL_DETAILS_MAP[model]
        kwargs.pop('model', None)
        kwargs['engine'] = model_details['engine']
        kwargs['api_key'] = model_details['api_key']
        kwargs['api_version'] = model_details['api_version']
        kwargs['api_base'] = model_details['api_base']
        kwargs['api_type'] = model_details['api_type']
        kwargs.pop('_open_ai_rate_limit_requests_per_minute', None)
        kwargs['_open_ai_rate_limit_requests_per_minute'] = model_details['properties']['rate_limit_(Requests per minute)']

    # requests_per_minute = kwargs.get('_open_ai_rate_limit_requests_per_minute', 3000)
    # delay_in_seconds = 60.0 / requests_per_minute
    # time.sleep(delay_in_seconds)

    kwargs.pop('_open_ai_rate_limit_requests_per_minute', None)
    kwargs.pop('_logger', None)
    kwargs.pop('_name', None)
    kwargs.pop('_rate_limiter', None)
    kwargs['input'] = replace_newlines(input)

    t0 = time.perf_counter()
    # if logger:
    #     logger.info(f"[{name}][OpenAI API Request] {kwargs}")
    # pretty_print_chat_messages(kwargs['messages'])
    embeddings = []
    if rate_limiter:
        # rate_limiter.consume(**kwargs)
        response = openai.Embedding.create(**kwargs)
        # response = get_embedding(**kwargs)
    else:
        response = openai.Embedding.create(**kwargs)
        # response = get_embedding(**kwargs)
    for i, be in enumerate(response["data"]):
        assert i == be["index"]  # double check embeddings are in same order as input
    batch_embeddings = [e["embedding"] for e in response["data"]]
    embeddings.extend(batch_embeddings)
    # if logger:
        # logger.info(f"[{name}][OpenAI API Returned] Elapsed request time: {time.perf_counter() - t0}s | response: {response}")
    return embeddings

def num_tokens_consumed_by_chat_request(messages, max_tokens=15, n=1, functions='', **kwargs):
    # num_tokens = n * max_tokens
    # for message in messages:
    #     num_tokens += 4 # Every message follows <im_start>{role/name}\n{content}<im_end>\n
    #     for key, value in message.items():
    #         num_tokens += len(CL100K_ENCODER.encode(str(value)))

    #         if key == "name": # If there's a name, the role is omitted
    #             num_tokens -= 1
            
    # num_tokens += 2 # Every reply is primed with <im_start>assistant
    num_tokens = num_tokens_from_messages(messages)


    if functions:
        function_tokens = num_tokens_from_functions(functions)
        num_tokens += function_tokens

    return num_tokens

def num_tokens_from_messages(messages, model="gpt-4-0613"):
    """Return the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    if model in {
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-16k-0613",
        "gpt-4-0314",
        "gpt-4-32k-0314",
        "gpt-4-0613",
        "gpt-4-32k-0613",
        }:
        tokens_per_message = 3
        tokens_per_name = 1
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif "gpt-3.5-turbo" in model:
        print("Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
        return num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613")
    elif "gpt-4" in model:
        print("Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
        return num_tokens_from_messages(messages, model="gpt-4-0613")
    else:
        raise NotImplementedError(
            f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            try:
                num_tokens += len(encoding.encode(value))
            except TypeError:
                num_tokens += len(encoding.encode(str(value)))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens


def num_tokens_from_functions(functions, model="gpt-3.5-turbo-0613"):
    """Return the number of tokens used by a list of functions."""
    num_tokens = 0
    for function in functions:
        function_tokens = len(CL100K_ENCODER.encode(function['name']))
        function_tokens += len(CL100K_ENCODER.encode(function['description']))
        
        if 'parameters' in function:
            parameters = function['parameters']
            if 'properties' in parameters:
                for propertiesKey in parameters['properties']:
                    function_tokens += len(CL100K_ENCODER.encode(propertiesKey))
                    v = parameters['properties'][propertiesKey]
                    for field in v:
                        if field == 'type':
                            function_tokens += 2
                            function_tokens += len(CL100K_ENCODER.encode(v['type']))
                        elif field == 'description':
                            function_tokens += 2
                            function_tokens += len(CL100K_ENCODER.encode(v['description']))
                        elif field == 'enum':
                            function_tokens -= 3
                            for o in v['enum']:
                                function_tokens += 3
                                function_tokens += len(CL100K_ENCODER.encode(o))
                        elif field == 'items':
                            # function_tokens += 2
                            # function_tokens += 2
                            function_tokens += len(CL100K_ENCODER.encode(v['type']))
                            if 'properties' in v[field]:
                                NestedParameters = v[field]
                                for NestedpropertiesKey in NestedParameters['properties']:
                                    function_tokens += len(CL100K_ENCODER.encode(NestedpropertiesKey))
                                    Nestedv = NestedParameters['properties'][NestedpropertiesKey]
                                    for Nestedfield in Nestedv:
                                        if Nestedfield == 'type':
                                            # function_tokens += 2
                                            function_tokens += len(CL100K_ENCODER.encode(Nestedv['type']))
                                        elif Nestedfield == 'description':
                                            # function_tokens += 2
                                            function_tokens += len(CL100K_ENCODER.encode(Nestedv['description']))
                                        elif Nestedfield == 'enum':
                                            function_tokens -= 3
                                            for Nestedo in Nestedv['enum']:
                                                # function_tokens += 3
                                                function_tokens += len(CL100K_ENCODER.encode(Nestedo))
                                        elif field == 'items':
                                            # function_tokens += 2
                                            # function_tokens += 2
                                            function_tokens += len(CL100K_ENCODER.encode(Nestedv['type']))

                                print('')
                        else:
                            print(f"Warning: not supported field {field} : {v[field]}")
                function_tokens += 11

        num_tokens += function_tokens

    num_tokens += 12 
    return num_tokens



if __name__ == "__main__":
    # Test OpenAI API
    if False:
        print(chat_completion_rl(
                    model="gpt-3.5-turbo",
                    messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": "Who won the world series in 2020?"},
                            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                            {"role": "user", "content": "Where was it played?"}
                        ],
                    max_tokens=5,
                    temperature=0.9,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0,
                    stop=["\n", "Human:", "AI:"]
                    ))
        
    # Test Azure API 
    if False:
        from rate_limiter import ChatRateLimiter
        rate_limiter = ChatRateLimiter(request_limit=200, token_limit=40000)
        print(chat_completion_rl(
                    # model="gpt-3.5-turbo",
                    model="gpt-4",
                    messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": "Who won the world series in 2020?"},
                            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                            {"role": "user", "content": "Where was it played?"}
                        ],
                    max_tokens=5,
                    temperature=0.9,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0,
                    stop=["\n", "Human:", "AI:"],
                    _use_azure_api=True,
                    _rate_limiter=rate_limiter
                    ))
    if True:
        # Test Embedding from Azure API
        # print(embedding_rl(text="The food was delicious and the waiter...",
        #                     model="text-embedding-ada-002",
        #                     _use_azure_api=True))
        # print(embedding_rl(text="The food was delicious and the waiter...",
        #                     model="text-embedding-ada-002",
        #                     _use_azure_api=True))
        # print('test batches')
        # print(embedding_rl(["The food was delicious and the waiter...", "had to see what was made for dinner", "then the waiter came back and said"]))
        print('test batches')
        print(embedding_rl('asdas'))
        