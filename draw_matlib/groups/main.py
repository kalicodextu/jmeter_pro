import sys
import numpy
from pylab import *

x_threads = numpy.array([0, 1, 10, 50, 100, 200, 400])

y_samples = numpy.array([0, 14930, 45174, 44946, 45377, 44066, 45837])
y_average = numpy.array([0, 20, 66, 333, 639, 1364, 2447])
y_tps = numpy.array([0, 49.8, 150.6, 149.8, 152.5, 143.7, 144.1])

if __name__ == '__main__':
    if sys.argv[1] == 'samples':
        plot(x_threads, y_samples, color='blue', label='samples(number of users)')
        # vlines(350, 0, 38000, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/samples.png')
        show()
    elif sys.argv[1] == 'average':                                                     
        plot(x_threads, y_average, color='blue', label='average')
        # vlines(200, 0, 3200, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/average.png')
        show()
    elif sys.argv[1] == 'tps':                                                     
        plot(x_threads, y_tps, color='blue', label='tps')
        # vlines(200, 0, 132, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/tps.png')
        show()
    else:
        print 'pass'
































