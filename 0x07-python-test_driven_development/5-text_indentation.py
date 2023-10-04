#!/usr/bin/python3
"""
This modual contains text_indentation function
"""


def text_indentation(text):
    """
    This function prints a new line when char == '.' or ':' or '?'

    Args:
        text: the string input

    Return:
        the new string

    Raises:
        TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    a = 0
    for i in range(len(text)):
        if text[i] in {".", "?", ":"}:
            print(f"{text[i]}\n")
            a = 1
        else:
            if a == 1:
                if text[i] == " ":
                    continue
                else:
                    print(f"{text[i]}", end="")
                    a = 0
            else:
                print(f"{text[i]}", end="")


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
