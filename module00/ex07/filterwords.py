import re
import sys


def filterwords(str, n):
    delimiters = '[ !#$%&*,-./:;<=>?@^_`}{~' + r'\"\'\(\)\+\[\]\|' + ']'
    filter_lst = re.split(delimiters, str)
    tmp = filter_lst.copy()
    for elem in tmp:
        if len(elem) <= n:
            filter_lst.remove(elem)
    return filter_lst


if len(sys.argv) != 3:
    print("ERROR")
else:
    try:
        n = int(sys.argv[2])
        filter_lst = filterwords(sys.argv[1], n)
        print(filter_lst)
    except ValueError:
        print('ERROR')
