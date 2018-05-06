import sys
import numpy
from pylab import *

x_threads = numpy.array([0, 1, 3, 5, 10, 50, 400])

y_samples = numpy.array([0, 11766, 27406, 28958, 31290, 30991, 29226])
y_average = numpy.array([0, 25, 32, 51, 95, 483, 4116])
y_tps = numpy.array([0, 39.2, 91.4, 96.5, 104.3, 103.2, 96.7])

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
































































