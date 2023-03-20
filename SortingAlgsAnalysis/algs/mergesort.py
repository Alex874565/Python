import time
import sys

sys.path.insert(0, "/home/alex874565/Desktop/Facultate/Python/Sortari/samples")
from samples import *

sys.setrecursionlimit(1000000)

array = shuffled_table(0, VAR_SIZE, TABLE_SIZE)

def interclasare(t1, stop1, t2, stop2):
    t = []
    i = 0
    j = 0
    while i <= stop1 and j <= stop2:
        if t1[i] <= t2[j]:
            t.append(t1[i])
            i += 1
        else:
            t.append(t2[j])
            j += 1
    while i <= stop1:
        t.append(t1[i])
        i += 1
    while j <= stop2:
        t.append(t2[j])
        j += 1
    return t

def mergesort(array, start, stop):
    t = []
    if start < stop:
        m = (start + stop)//2
        t1 = mergesort(array, start, m)
        t2 = mergesort(array, m+1, stop)
        t = interclasare(t1, m - start, t2, stop - m-1)
    else:
        t.append(array[start])
    return t

# print("Mergesort: ")

start_time = time.time()
mergesort(array, 1, TABLE_SIZE)
stop_time = time.time()
duration = stop_time - start_time
print(f"{duration:.10f}")
