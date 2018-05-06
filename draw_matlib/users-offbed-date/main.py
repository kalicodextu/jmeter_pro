import sys
import numpy
from pylab import *
from matplotlib import ticker

x_threads = numpy.array([0, 1, 2, 3, 4, 5, 10, 15, 20])

y_samples = numpy.array([0, 11853, 23260, 29857, 33812, 33926, 36803, 33609, 34944])
y_average = numpy.array([0, 25, 25, 29, 35, 44, 81, 133, 171])
y_tps = numpy.array([0, 39.5, 77.5, 99.5, 112.7, 113.1, 122.7, 112, 116.5])

if __name__ == '__main__':
    if sys.argv[1] == 'samples':
        plot(x_threads, y_samples, color='blue', label='samples(number of users)')
        # vlines(200, 0, 50000, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/samples.png')
        show()
    elif sys.argv[1] == 'average':                                                     
        plot(x_threads, y_average, color='blue', label='average')
        # vlines(200, 0, 2900, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/average.png')
        show()
    elif sys.argv[1] == 'tps':                                                     
        plot(x_threads, y_tps, color='blue', label='tps')
        # vlines(200, 0, 165, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/tps.png')
        show()
    else:
        print 'pass'

