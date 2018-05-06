import sys
import numpy
from pylab import *

x_threads = numpy.array([0, 1, 2, 3, 4, 5, 10, 50])

y_samples = numpy.array([0, 12025, 22467, 29568, 33122, 34988, 34912, 35097])
y_average = numpy.array([0, 24, 26, 30, 36, 43, 85, 427])
y_tps = numpy.array([0, 24.31, 45.42, 59.78, 66.97, 70.74, 70.58, 70.9])

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
































































