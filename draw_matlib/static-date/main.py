import sys
import numpy
from pylab import *

x_threads = numpy.array([0, 1, 2, 3, 4, 5, 10])

y_samples = numpy.array([0, 10446, 17235, 20746, 21210, 21654, 21267])
y_average = numpy.array([0, 28, 34, 43, 56, 69, 140])
y_tps = numpy.array([0, 34.8, 57.5, 69.2, 70.7, 72.2, 70.9])

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
































































