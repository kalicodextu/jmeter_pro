import sys
import numpy
from pylab import *

x_threads = numpy.array([0, 1, 2, 3, 4, 5, 10, 50])

y_samples = numpy.array([0, 12512, 22124, 29495, 32051, 32751, 35011, 33572])
y_average = numpy.array([0, 23, 26, 30, 37, 45, 85, 446])
y_tps = numpy.array([0, 41.7, 73.8, 98.3, 106.8, 109.2, 116.7, 111.8])

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
































































