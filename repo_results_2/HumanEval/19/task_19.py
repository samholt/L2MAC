from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    numeral_to_int = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    int_to_numeral = {v: k for k, v in numeral_to_int.items()}

    numerals = numbers.split()
    ints = [numeral_to_int[numeral] for numeral in numerals]
    sorted_ints = sorted(ints)
    sorted_numerals = [int_to_numeral[i] for i in sorted_ints]

    return ' '.join(sorted_numerals)
