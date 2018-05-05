import sys
import numpy
from pylab import *

x_threads = numpy.array([0, 500, 1000, 5000, 10000, 20000, 30000, 40000, 50000,
    80000, 100000, 500000])

y_redis_average= numpy.array([29.3, 29.5, 28.8, 29.1, 29.8, 28.8, 30.2,
    31.8, 29.6, 28.6, 29.4, 29.6])

if __name__ == '__main__':
    plot(x_threads, y_redis_average, color='darkblue')
    ylim(0, 32)
    savefig('./pic/redis.png')
    show()































































