# File timerdeco1.py

from threading import Timer
import time
import sys


class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0

    def __call__(self, *args, **kargs):
        start = time.perf_counter()
        result = self.func(*args, **kargs)
        elapsed = time.perf_counter() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result


@timer
def listcomp(N):
    return [x*2 for x in range(N)]


@timer
def mapcall(N):
    return list(map((lambda x: x*2), range(N)))


result = listcomp(5)
listcomp(500000)
print(result)
print('allTime = %s' % listcomp.alltime)

print(' ')
result = mapcall(5)
mapcall(500000)
print(result)
print('allTime = %s' % mapcall.alltime)

print('\n**map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))
