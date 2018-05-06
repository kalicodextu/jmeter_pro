import sys
import numpy
from pylab import *

x_threads = numpy.array([0, 1, 10, 50, 100, 200, 300, 350, 400])

y_samples = numpy.array([0, 6164, 32355, 31759, 34691, 39363, 36888, 37128, 37652])
y_average = numpy.array([0, 48, 92, 472, 866, 1526, 2447, 2878, 3199])
y_tps = numpy.array([0, 20.5, 107.8, 105.8, 115.4, 130.8, 122.2, 124.3, 124.5])

if __name__ == '__main__':
    if sys.argv[1] == 'samples':
        plot(x_threads, y_samples, color='blue', label='samples(number of users)')
        vlines(350, 0, 38000, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/samples.png')
        show()
    elif sys.argv[1] == 'average':                                                     
        plot(x_threads, y_average, color='blue', label='average')
        vlines(350, 0, 3200, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/average.png')
        show()
    elif sys.argv[1] == 'tps':                                                     
        plot(x_threads, y_tps, color='blue', label='tps')
        vlines(350, 0, 132, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/tps.png')
        show()
    else:
        print 'pass'
































