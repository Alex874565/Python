import time
import sys

sys.path.insert(0, "/home/alex874565/Desktop/Facultate/Python/Sortari/samples")
from samples import *

array= ordered_table(L_VAR, XL_VAR, XL_TABLE)

def shakersort(array, n, file):
    start_time = time.time()
    s = 1
    d = n

    t = 0
    for i in range(s, d):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            t = i
    if t!= 0:
        d = t
        t = 0
        for i in range(d, s, -1):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
                t = i
    s = t

    while(t!=0 and s != d):
        t = 0
        for i in range(s, d):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                t = i
        if t!= 0:
            d = t
            t = 0
            for i in range(d, s, -1):
                if array[i] < array[i-1]:
                    array[i], array[i-1] = array[i-1], array[i]
                    t = i
        s = t
    stop_time = time.time()
    duration = stop_time - start_time
    print(f"{duration:.10f}")
    # with open(file, 'a') as file:
    #    file.write(f"{duration:.10f}")
    return array

# print("Shakersort: ")
shakersort(array, XL_TABLE, "")