#!/usr/bin/python3
def text_indentation(text):
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
