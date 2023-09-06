#!/usr/bin/python3

"""Defines a text-indentation function."""
def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    val = 0
    while val < len(text) and text[val] == ' ':
        val += 1

    while val < len(text):
        print(text[val], end="")
        if text[val] == "\n" or text[val] in ".?:":
            if text[val] in ".?:":
                print("\n")
            val += 1
            while val < len(text) and text[val] == ' ':
                val += 1
            continue
        val += 1

