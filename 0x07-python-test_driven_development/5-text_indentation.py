#!/usr/bin/python3
"""
Text indentation module

This module prints a text with 2 new lines after each of these characters:
., ? and :. The text must be a string.
Otherwise raise a TypeError exception with custom error messages.
"""


def text_indentation(text):
    """
    Pints a text with 2 new lines after each of these characters:., ? and :
    Arguments:
    @text: text to indentate

    Returns:
    Nothing; only prints the new text, otherwise raise a TypeError
    when text is not a string

    Example:
    >>> text_indentation("Hello.World")
    Hello.

    World
    """
    if type(text) is not str or text is None or len(text) < 0:
        raise TypeError("text must be a string")
    text = text.strip()
    flag = False
    symbols = ['.', '?', ':']
    for c in text:
        if c == ' ' and flag is True:
            continue
            flag = False
        if c in symbols:
            print(c)
            print()
            flag = True
        else:
            print(c, end="")
            flag = False
