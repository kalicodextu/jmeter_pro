import sys
import numpy
from pylab import *

x_threads = numpy.array([0, 1, 10, 20, 30, 40, 50, 100, 150, 200, 400])

y_samples = numpy.array([0, 5893, 25055, 22256, 21922, 32659, 36334, 37546,
    33754, 31061, 28028])
y_average = numpy.array([0, 50, 199, 269, 411, 367, 412, 800, 1342, 1944, 4294])
y_tps = numpy.array([0, 19.6, 83.3, 74.2, 72.4, 108.8, 121, 124.9, 110, 101.3,
    87.8])

if __name__ == '__main__':
    if sys.argv[1] == 'samples':
        plot(x_threads, y_samples, color='blue', label='samples(number of users)')
        vlines(200, 0, 38000, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/samples.png')
        show()
    elif sys.argv[1] == 'average':                                                     
        plot(x_threads, y_average, color='blue', label='average')
        vlines(200, 0, 4300, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/average.png')
        show()
    elif sys.argv[1] == 'tps':                                                     
        plot(x_threads, y_tps, color='blue', label='tps')
        vlines(200, 0, 130, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/tps.png')
        show()
    else:
        print 'pass'
































