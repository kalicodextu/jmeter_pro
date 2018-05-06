import sys
import numpy
from pylab import *

x_threads = numpy.array([0, 1, 10, 20, 30, 40, 50, 100, 200, 400])

y_samples = numpy.array([0, 3720, 3837, 3514, 3455, 3495, 3510, 3454, 3487,
    3506])
y_average = numpy.array([0, 80, 782, 1693, 2580, 3386, 4297, 7044, 10623,
    16588])
y_tps = numpy.array([0, 12.4, 12.7, 11.7, 11.5, 11.7, 11, 11.5, 11.7, 11.7])

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
