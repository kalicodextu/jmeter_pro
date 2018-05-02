import sys
import numpy
from pylab import *

x_threads = numpy.array([1, 10, 50, 100, 200, 300, 400, 500])

y_samples = numpy.array([3255, 16161, 17997, 28788, 35309, 39575, 41781, 40063])
y_average = numpy.array([92, 185, 834, 1045, 1703, 2280, 2882, 3764])
y_tps = numpy.array([10.8, 53, 59.9, 94.9, 98.4, 131.4, 137.8, 128.4])

if __name__ == '__main__':
    if sys.argv[1] == 'samples':
        plot(x_threads, y_samples, color='blue', label='samples(number of users)')
        vlines(450, 0, 45000, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/samples.png')
        show()
    elif sys.argv[1] == 'average':                                                     
        plot(x_threads, y_average, color='blue', label='average')
        vlines(450, 0, 4000, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/average.png')
        show()
    elif sys.argv[1] == 'tps':                                                     
        plot(x_threads, y_tps, color='blue', label='tps')
        vlines(450, 0, 140, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/tps.png')
        show()
    else:
        print 'pass'
