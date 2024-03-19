from typing import List


def string_xor(a: str, b: str) -> str:
    """ 
    This function takes two binary strings a and b as input.
    It performs a binary XOR operation on these inputs and returns the result as a string.
    If the lengths of a and b are not equal, it raises a ValueError.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the XOR operation.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    if len(a) != len(b):
        raise ValueError('Input strings must have the same length')
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
