class Evaluator:
    def zip_evaluate(coefs, words):
        if isinstance(coefs, list) is False or \
                isinstance(words, list) is False or \
                len(coefs) != len(words) or \
                len(coefs) == 0:
            return -1
        ret = 0
        for coef, word in zip(coefs, words):
            if isinstance(coef, float) is False or \
                    isinstance(word, str) is False:
                return -1
            ret += coef * len(word)
        return ret

    def enumerate_evaluate(coefs, words):
        if isinstance(coefs, list) is False or \
                isinstance(words, list) is False or \
                len(coefs) != len(words) or \
                len(coefs) == 0:
            return -1
        ret = 0
        for i, coef in enumerate(coefs):
            if isinstance(coef, float) is False or \
                    isinstance(words[i], str) is False:
                return -1
            ret += coef * len(words[i])
        return ret
