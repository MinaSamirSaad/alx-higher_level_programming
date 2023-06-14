#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    Roman_numerals = {'I': 1, 'V': 5, 'X': 10,'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    before = 0
    for i in reversed(roman_string):
        num = Roman_numerals[i]
        sum = sum + num if num >= before else sum - num
        before = num
    return sum
