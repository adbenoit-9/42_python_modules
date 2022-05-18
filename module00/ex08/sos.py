import sys


def str_to_morse(str):
    morse = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.'
    }
    ret = ""
    for c in str:
        if c == ' ':
            ret += '/'
        elif c.upper() in morse.keys():
            ret += morse[c.upper()]
        else:
            return 1, ""
        ret += " "
    return 0, ret


output = ""
size = len(sys.argv)
if size != 1:
    for i in range(1, size):
        err, morse = str_to_morse(sys.argv[i])
        if err == 1:
            break
        output += morse
        if i != size - 1:
            output += '/ '
    if err == 1:
        print('ERROR')
    else:
        print(output)
