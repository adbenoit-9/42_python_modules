import string

def text_analyzer(*args, **kwargs):
    '''This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.'''
    if len(args) > 1:
        print("ERROR")
        return
    elif len(args) < 1:
        text = input("What is the text to analyse? ")
    else:
        text = args[0]
    uppercase = 0
    lowercase = 0
    punct = 0
    space = 0
    for c in text:
        if c.isupper():
            uppercase += 1;
        elif c.islower():
            lowercase += 1;
        elif c == " ":
            space += 1
        else:
            for i in string.punctuation:
                if c == i:
                    punct += 1
    print("the text contains " + str(len(text)) + " characters:\n"
    + "- " + str(uppercase) + " upper letters\n"
    + "- " + str(lowercase) + " lower letters\n"
    + "- " + str(punct) + " punctuation marks\n"
    + "- " + str(space) + " spaces\n")
    return