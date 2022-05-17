from progressbar import ProgressBar
import time

def ft_progress(lst):
    p = 0
    print('\r{}%  |#'.format(p))
    return lst

listy = range(1000)
pbar = ProgressBar()
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)

