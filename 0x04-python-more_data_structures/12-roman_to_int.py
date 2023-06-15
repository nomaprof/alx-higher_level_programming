#!/usr/bin/python3
def roman_to_int(roman_string):
    """ converts a Roman numeral to an integer."""
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return 0

    answer = len(roman_string)
    param = romans[roman_string[answer-1]]
    for i in range(answer - 1, 0, -1):
        recent_ans = romans[roman_string[i]]
        past_ans = romans[roman_string[i-1]]

        if past_ans >= recent_ans:
            param += past_ans
        else:
            param -= past_ans

    return param
