import scipy.signal as sps
import math
import timeit
import matplotlib.pyplot as plt

def find_peaks(data):
    peaks = []
    for t in range(1,len(data)-1):
        if data[t]>data[t-1] and data[t+1]<data[t]:
            peaks.append(t)
    return peaks

def find_peaks_2(data):
    peaks = []
    ascending = (data[1] > data[0])
    for t in range(1,len(data)-1):
        first = data[t]
        second = data[t+1]
        if ascending and second<first:
            peaks.append(t)
        ascending = (second>first)
    return peaks

p = [math.sin(2*math.pi*.01*i) for i in range(10000)]
print(sps.find_peaks(p)) # expected at 25, 125, 225, ...
print(find_peaks(p))
print(find_peaks_2(p))
n = [10,100,1000]
t1 = []
t2 = []
t3 = []
t1.append(timeit.timeit('sps.find_peaks(p)',number=10,globals=globals()))
t2.append(timeit.timeit('find_peaks(p)',number=10,globals=globals()))
t3.append(timeit.timeit('find_peaks_2(p)',number=10,globals=globals()))
t1.append(timeit.timeit('sps.find_peaks(p)',number=100,globals=globals()))
t2.append(timeit.timeit('find_peaks(p)',number=100,globals=globals()))
t3.append(timeit.timeit('find_peaks_2(p)',number=100,globals=globals()))
t1.append(timeit.timeit('sps.find_peaks(p)',number=1000,globals=globals()))
t2.append(timeit.timeit('find_peaks(p)',number=1000,globals=globals()))
t3.append(timeit.timeit('find_peaks_2(p)',number=1000,globals=globals()))
plt.plot(n,t1,n,t2,n,t3)
plt.legend(['SciPy','Implementation 1','Implementation 2'])
plt.show()
