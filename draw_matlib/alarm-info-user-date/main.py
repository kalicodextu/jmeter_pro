import sys
import numpy
from pylab import *

x_threads = numpy.array([0, 1, 10, 50, 100, 200, 250, 300, 400, 500])

y_samples = numpy.array(
    [0, 6601, 22583, 32824, 35537, 36792, 37142, 34156, 33724, 37007])
y_average = numpy.array([0, 45, 132, 457, 844, 1635, 2022, 2642, 3562, 4067])
y_tps = numpy.array([0, 22, 75.3, 109.3, 118.2, 121.7, 123.4, 113.3, 111.8, 122.5])

if __name__ == '__main__':
    if sys.argv[1] == 'samples':
        plot(
            x_threads,
            y_samples,
            color='blue',
            label='samples(number of users)')
        vlines(300, 0, 38000, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/samples.png')
        show()
    elif sys.argv[1] == 'average':
        plot(x_threads, y_average, color='blue', label='average')
        vlines(300, 0, 4100, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/average.png')
        show()
    elif sys.argv[1] == 'tps':
        plot(x_threads, y_tps, color='blue', label='tps')
        vlines(300, 0, 130, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/tps.png')
        show()
    else:
        print 'pass'
