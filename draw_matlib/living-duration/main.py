import sys
import numpy
from pylab import *

x_threads = numpy.array([0, 1, 10, 50, 100, 200, 400])

y_samples = numpy.array([0, 4432, 4640, 4573, 4774, 4753, 4494])
y_average = numpy.array([0, 67, 651, 2995, 4682, 6416, 9242])
y_tps = numpy.array([0, 14.8, 15.2, 14.7, 15.6, 14.8, 14.6])

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
































































