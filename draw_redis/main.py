import sys
import numpy
from pylab import *

x_threads = numpy.array([0, 1, 100, 1000, 2500, 5000, 7000, 10000])

y_redis_average= numpy.array([0, 4, 225, 2544, 6588, 12852, 17653, 25669])
y_origin_average = numpy.array([0, 4, 212, 2475, 6561, 12777, 18150, 25901])

y_redis_tps= numpy.array([0, 223.2, 439.5, 389.8, 374.2, 376.7, 371, 371])
y_origin_tps = numpy.array([0, 225.2, 467.9, 400.8, 369.4, 383.9, 380.8, 373.4])

if __name__ == '__main__':
    if sys.argv[1] == 'samples':
        print 'pass'
        # plot(x_threads, y_samples, color='blue', label='samples(number of users)')
        # # vlines(200, 0, 50000, color='red', linestyles='dashed', label='Error Line')
        # legend(loc='upper left')
        # savefig('./pic/samples.png')
        # show()
    elif sys.argv[1] == 'average':                                                     
        plot(x_threads, y_origin_average, color='darkcyan', label='origin')
        plot(x_threads, y_redis_average, color='gold', label='Redis')
        legend(loc='upper left')
        savefig('./pic/average.png')
        show()
    elif sys.argv[1] == 'tps':                                                     
        plot(x_threads, y_origin_tps, color='darkcyan', label='origin')
        plot(x_threads, y_redis_tps, color='gold', label='Redis')
        # vlines(200, 0, 165, color='red', linestyles='dashed', label='Error Line')
        legend(loc='upper left')
        savefig('./pic/tps.png')
        show()
    else:
        print 'pass'
































































