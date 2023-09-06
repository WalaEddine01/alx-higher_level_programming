#!/usr/bin/python3
for i in range(0, 26):
    if chr(97 + i) != 'e' and chr(97 + i) != 'q':
        print("{}".format(chr(97 + i)), end="")
    else:
        continue
