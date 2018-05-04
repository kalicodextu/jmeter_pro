import sys
import numpy
from pylab import *

x_threads = numpy.array([0, 1, 10, 50, 100, 200, 400])

y_samples = numpy.array([0, 15067, 41383, 46124, 46482, 45522, 45414])
y_average = numpy.array([0, 19, 72, 325, 645, 1319, 2648])
y_tps = numpy.array([0, 50.2, 138, 153.6, 154.2, 151.4, 138.1])

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
































