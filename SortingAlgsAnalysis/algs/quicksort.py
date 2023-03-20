import time
import sys
import resource

resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.path.insert(0, "/home/alex874565/Desktop/Facultate/Python/Sortari/samples")
from samples import *

sys.setrecursionlimit(1000000)

array = shuffled_table(0, VAR_SIZE, TABLE_SIZE)

def pivot(array, start, stop):
    v = array[stop]
    i = start - 1
    j = stop
    while i < j:
        i = i + 1
        while array[i] < v:
            i += 1
        j -= 1
        while array[j] != '' and array[j] > v:
            j -= 1
        if i < j:
            array[i],array[j] = array[j],array[i]
    array[i], array[stop] = array[stop], array[i]
    return i

def  quicksort(array, start, stop):
    t = []
    if start < stop:
        q = pivot(array, start, stop)
        t1 = quicksort(array, start, q-1)
        t2 = quicksort(array, q+1, stop)
        t = t1
        t.append(array[q])
        t += t2
    return t

# print("Quicksort: ")

start_time = time.time()
quicksort(array, 1, TABLE_SIZE)
stop_time = time.time()
duration = stop_time - start_time
print(f"{duration:.10f}")
