#!/usr/bin/python

import sys

size = len(sys.argv)
ret = ""
for i in range(1, size):
    if i > 1:
        ret += " "
    ret += sys.argv[i][::-1].swapcase()
print(ret)
