from numpy import genfromtxt
import talib

my_data = genfromtxt('15_min.csv', delimiter=',')

time = my_data[:,0]
close = my_data[:,4]

# print(close)
# close = numpy.random.random(100)

# print(close)

# moving_average = talib.SMA(close, timeperiod=10)
# print(moving_average)

rsi = talib.RSI(close)
i = 0
for value in rsi:
    print(str(value) + " " + str(time[i]))
    i+=1
