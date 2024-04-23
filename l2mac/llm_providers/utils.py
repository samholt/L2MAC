from difflib import get_close_matches


def find_best_match(data_dict, model_name, n=1):
    """
    Find the best matching model name from the provided dictionary keys.

    Args:
    - data_dict (dict): Dictionary of models with their details.
    - model_name (str): The model name to match.
    - n (int): Number of close matches to return; default is 1.

    Returns:
    - dict or None: Returns the dictionary of the closest match, or None if no match is found.
    """
    # Retrieve close matches from the dictionary keys
    matches = get_close_matches(model_name, data_dict.keys(), n=n, cutoff=0.0)
    if matches:
        return data_dict[matches[0]]  # Return the best match's details
    return None  # Return None if no matches found


def pretty_print_chat_messages(
    messages,
    num_tokens=None,
    max_tokens=None,
    logger=None,
    response_msg=False,
    step_idx=None,
    total_steps=None,
    max_re_tries=None,
    re_tries=None,
):
    COLORS = {
        "system": "\033[95m",  # Light Magenta
        "user": "\033[94m",  # Light Blue
        "assistant": "\033[92m",  # Light Green
        "tokens": "\033[91m",  # Light Red
    }

    if response_msg:
        print("[LLM RESPONSE MESSAGE]")  # Reset color at the end
        if logger:
            logger.info("[LLM RESPONSE MESSAGE]")

    for msg in messages:
        role = msg["role"]
        color = COLORS.get(role, COLORS["system"])  # Default to system color if role not found
        formatted_role = role.capitalize()
        if role == "assistant" and msg.get("tool_calls", False):
            formatted_role = "Function Call"
            for tool_call in msg["tool_calls"]:
                print(
                    f"{color}[{formatted_role}] [{tool_call['function']['name']}] {tool_call['function']['arguments']}\033[0m"
                )  # Reset color at the end
                if logger:
                    logger.info(
                        f"[{formatted_role}] [{tool_call['function']['name']}] {tool_call['function']['arguments']}"
                    )
        else:
            content = msg.get("content", None)
            print(f"{color}[{formatted_role}] {content}\033[0m")  # Reset color at the end
            if logger:
                logger.info(f"[{formatted_role}] {content}")

    if not response_msg:
        if step_idx is not None and total_steps is not None:
            if num_tokens and max_tokens:
                if max_re_tries is not None and re_tries is not None:
                    print(
                        f"{COLORS['tokens']}[Progress: Step {step_idx + 1}/{total_steps} | Retries: {re_tries}/{max_re_tries} | Token Capacity Used: {((num_tokens / max_tokens) * 100.0):.2f}% | Tokens remaining {max_tokens - num_tokens}]\033[0m"
                    )
                    if logger:
                        logger.info(
                            f"[Progress: Step {step_idx + 1}/{total_steps} | Retries: {re_tries}/{max_re_tries} | Token Capacity Used: {((num_tokens / max_tokens) * 100.0):.2f}% | Tokens remaining {max_tokens - num_tokens}]"
                        )
                else:
                    print(
                        f"{COLORS['tokens']}[Progress: Step {step_idx + 1}/{total_steps} | Token Capacity Used: {((num_tokens / max_tokens) * 100.0):.2f}% | Tokens remaining {max_tokens - num_tokens}]\033[0m"
                    )
                    if logger:
                        logger.info(
                            f"[Progress: Step {step_idx + 1}/{total_steps} | Token Capacity Used: {((num_tokens / max_tokens) * 100.0):.2f}% | Tokens remaining {max_tokens - num_tokens}]"
                        )

        else:
            if num_tokens and max_tokens:
                print(
                    f"{COLORS['tokens']}[Token Capacity Used: {((num_tokens / max_tokens) * 100.0):.2f}% | Tokens remaining {max_tokens - num_tokens}]\033[0m"
                )
                if logger:
                    logger.info(
                        f"[Token Capacity Used: {((num_tokens / max_tokens) * 100.0):.2f}% | Tokens remaining {max_tokens - num_tokens}]"
                    )
