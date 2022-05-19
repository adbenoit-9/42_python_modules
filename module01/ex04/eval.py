class Evaluator:
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        ret = 0
        for coef, word in zip(coefs, words):
            ret += coef * len(word)
        return ret

    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        ret = 0
        for i, coef in enumerate(coefs):
            ret += coef * len(words[i])
        return ret
