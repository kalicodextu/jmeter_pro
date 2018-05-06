import sys
import numpy
from pylab import *

x_threads = numpy.array([0, 1, 3, 5, 10, 50, 400])

y_samples = numpy.array([0, 11842, 27625, 34133, 35431, 35429, 33856])
y_average = numpy.array([0, 25, 32, 43, 84, 423, 3555])
y_tps = numpy.array([0, 39.5, 92.1, 113.8, 118.1, 118, 112.1])

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
































































