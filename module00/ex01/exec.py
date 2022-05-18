import sys

size = len(sys.argv)
ret = ""
for i in range(size - 1, 0, -1):
    if i < size - 1:
        ret += " "
    ret += sys.argv[i][::-1].swapcase()
if size > 1:
    sys.stdout.write(ret + '\n')
