import sys
import numpy
from pylab import *

x_threads = numpy.array([0, 1, 10, 25, 35, 40, 45, 50, 60, 70, 80, 90, 100, 200,
    400])

y_samples = numpy.array([0, 3249, 3963, 3932, 3778, 3701, 3532, 3727, 3321, 3948,
    3987, 4053, 4005, 3959, 3915])
y_average = numpy.array([0, 92, 756, 1914, 2793, 3153, 3746, 3881, 5342, 4596,
    5232, 6203, 6632, 11029, 15383])
y_tps = numpy.array([0, 10.8, 13, 12.4, 12.3, 12.1, 11.6, 12.5, 11.1, 13.5, 13.4,
    13.4, 13.3, 13.3, 12.9])

if __name__ == '__main__':
    if sys.argv[1] == 'samples':
        plot(x_threads, y_samples, color='blue', label='samples(number of users)')
        # vlines(450, 0, 45000, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/samples.png')
        show()
    elif sys.argv[1] == 'average':                                                     
        plot(x_threads, y_average, color='blue', label='average')
        # vlines(450, 0, 4000, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/average.png')
        show()
    elif sys.argv[1] == 'tps':                                                     
        plot(x_threads, y_tps, color='blue', label='tps')
        # vlines(450, 0, 140, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/tps.png')
        show()
    else:
        print 'pass'
