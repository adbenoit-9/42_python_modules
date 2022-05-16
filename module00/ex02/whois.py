#!/usr/bin/python

import sys

size = len(sys.argv)
if size < 2:
    ret = ""
elif size > 2:
    ret = "AssertionError: more than one argument is provided"
else:
    try:
        nb = int(sys.argv[1])
        if nb == 0:
            ret = "I'm Zero."
        elif nb % 2 == 0:
            ret = "I'm Even."
        else:
            ret = "I'm Odd."
    except ValueError:
        ret = "AssertionError: argument is not integer"
print(ret)
