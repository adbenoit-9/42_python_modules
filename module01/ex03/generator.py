import random as rd


def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    if isinstance(text, str) is False:
        yield "ERROR"
        return
    words_list = text.split(sep)
    n = len(words_list)
    if option is None:
        for word in words_list:
            yield word
    elif option == "shuffle":
        index_list = []
        for i in range(n):
            random_index = rd.randint(0, n - 1)
            while random_index in index_list:
                random_index = rd.randint(0, n - 1)
            index_list.append(random_index)
            yield words_list[random_index]
    elif option == "unique":
        new_list = []
        for word in words_list:
            if word not in new_list:
                new_list.append(word)
                yield word
    elif option == "ordered":
        for word in sorted(words_list):
            yield word
    else:
        yield "ERROR"
