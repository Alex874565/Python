import time
import sys

sys.path.insert(0, "/home/alex874565/Desktop/Facultate/Python/Sortari/samples")
from samples import *

array= shuffled_table(pow(10, 8), pow(10,9), XL_TABLE)



def countingsort(array, n, file):
    f = []
    y = []
    max = array[1]
    for i in range(n):
        y.append(0)
    for num in array[1:]:
        if num > max:
            max = num
    start_time = time.time()
    for i in range(max+1):
        f.append(0)
    for i in range(1,n):
        f[array[i]] = f[array[i]] + 1
    for i in range(2, max+1):
        f[i] = f[i-1] + f[i]
    for i in range(n-1, 0, -1):
        y[f[array[i]]] = array[i]
        f[array[i]] = f[array[i]] - 1
    for i in range(1, n):
        array[i] = y[i]
    stop_time = time.time()
    duration = stop_time - start_time
    print(f"{duration:.10f}")
    # with open(file, 'a') as file:
    #    file.write(f"{duration:.10f}")
    return array

countingsort(array, XL_TABLE, "")