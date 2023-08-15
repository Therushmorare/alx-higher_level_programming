#!/usr/bin/python3
#3. When I was having that alphabet soup, I never thought that it would pay off

for x in range(97, 123):
    if chr(x) is not 'q' and chr(x) is not 'e':
        print("{}".format(chr(x)), end="")
