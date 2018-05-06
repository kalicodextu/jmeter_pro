import sys
import numpy
from pylab import *

x_threads = numpy.array([0, 1, 5, 10, 50, 100, 400])

y_samples = numpy.array([0, 12232, 46987, 47487, 47055, 47026, 44789])
y_average = numpy.array([0, 24, 31, 63, 318, 637, 2684])
y_tps = numpy.array([0, 41.8, 156.6, 158.3, 156.8, 156.6, 148.6])

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
































































