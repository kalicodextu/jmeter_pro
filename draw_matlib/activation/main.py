import sys
import numpy
from pylab import *

x_threads = numpy.array([1, 10, 50, 100, 200, 250, 300, 400])

y_samples = numpy.array([4552, 14992, 25922, 30708, 31147, 32426, 35628, 33024])
y_average = numpy.array([65, 200, 578, 978, 1931, 2144, 2538, 3649])
y_tps = numpy.array([15.2, 50, 86.3, 102.1, 103, 107, 117.6, 83.7])

if __name__ == '__main__':
    if sys.argv[1] == 'samples':
        plot(x_threads, y_samples, color='blue', label='samples(number of users)')
        vlines(250, 0, 45000, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/samples.png')
        show()
    elif sys.argv[1] == 'average':                                                     
        plot(x_threads, y_average, color='blue', label='average')
        vlines(250, 0, 4000, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/average.png')
        show()
    elif sys.argv[1] == 'tps':                                                     
        plot(x_threads, y_tps, color='blue', label='tps')
        vlines(250, 0, 120, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/tps.png')
        show()
    else:
        print 'pass'
