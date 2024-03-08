import json

def serializable(obj):
    """
    Check if an object is serializable.
    """
    try:
        json.dumps(obj)
        return True
    except (TypeError, OverflowError):
        return False

def dump_locals_to_json(local_vars):
    """
    Dump local variables to a JSON format if they're serializable.
    """
    serializable_vars = {k: v for k, v in local_vars.items() if serializable(v)}
    return json.dumps(serializable_vars, indent=4)