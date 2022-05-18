import time
import sys


def ft_progress(lst):
    size = len(lst)
    length = len(str(size))
    t0 = time.time()
    t = t0
    for i in range(0, size):
        p = round(100 * i / size)
        n = round(i * 20 / size)
        tmp = t
        t = time.time() - t0
        if t - tmp < 0:
            eta = 0
        else:
            eta = (t - tmp) * (size - i - 1)
        anim = ">"
        anim = anim.rjust(n, '=')
        anim = anim.ljust(20, ' ')
        sys.stdout.write("""\rETA: {eta:5.2f}s [{percent:3d}%] [{anim}]\
{i:{maxlen}d}/{size} | elapsed time {time:.2f}s"""
                         .format(eta=eta, percent=p, anim=anim, i=i + 1,
                                 size=size, maxlen=length, time=t))
        yield i
