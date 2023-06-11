#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = None if not sentence else sentence[0]
    return len(sentence), first_char
