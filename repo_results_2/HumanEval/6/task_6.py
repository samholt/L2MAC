from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Split the input string into groups
    groups = paren_string.split()

    # Initialize an empty list to store the results
    results = []

    # Process each group
    for group in groups:
        # Initialize the current level of nesting and the maximum level of nesting
        current_level = max_level = 0

        # Process each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase the current level of nesting
            if char == '(':
                current_level += 1
                # If the current level of nesting is greater than the maximum level of nesting, update the maximum level of nesting
                if current_level > max_level:
                    max_level = current_level
            # If the character is a closing parenthesis, decrease the current level of nesting
            elif char == ')':
                current_level -= 1

        # Add the maximum level of nesting to the results list
        results.append(max_level)

    # Return the results list
    return results
