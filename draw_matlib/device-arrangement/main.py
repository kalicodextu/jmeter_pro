import sys
import numpy
from pylab import *

x_threads = numpy.array([0, 1, 10, 20, 30, 40, 50, 100, 200, 400])

y_samples = numpy.array([0, 7046, 18951, 20599, 22349, 22663, 22407, 22369,
    22485, 20890])
y_average = numpy.array([0, 42, 160, 291, 402, 507, 643, 999, 1516,
    2840])
y_tps = numpy.array([0, 23.5, 62.4, 68.6, 74.3, 69.3, 69.4, 68.6, 75.2, 70.4])

if __name__ == '__main__':
    if sys.argv[1] == 'samples':
        plot(x_threads, y_samples, color='blue', label='samples(number of users)')
        # vlines(450, 0, 45000, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/samples.png')
        show()
    elif sys.argv[1] == 'average':                                                     
        plot(x_threads, y_average, color='blue', label='average')
        # vlines(450, 0, 4000, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/average.png')
        show()
    elif sys.argv[1] == 'tps':                                                     
        plot(x_threads, y_tps, color='blue', label='tps')
        # vlines(450, 0, 140, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/tps.png')
        show()
    else:
        print 'pass'
