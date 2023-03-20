import time
import sys
import math

sys.path.insert(0, "/home/alex874565/Desktop/Facultate/Python/Sortari/samples")
from samples import *

array= ordered_table(0, XS_VAR, XS_TABLE)

y = ['']
for i in range(XL_TABLE):
    y.append(0)

def counting2(array, y, n, m, c):
    f = []
    for i in range(m+1):
        f.append(0)
    for i in range(1, n + 1):
        j = (array[i] // pow(10, c)) % 10
        f[j] = f[j] + 1
    for i in range(1, m+1):
        f[i] = f[i-1] + f[i]
    for i in range(n, 0, -1):
        j = (array[i] // pow(10, c)) % 10
        y[f[j]] = array[i]
        f[j] = f[j]-1
    return y

def radixsort(array, n, k, file):
    start_time = time.time()
    for i in range(0, k):
        array = counting2(array, y, n, 9, i)
    stop_time = time.time()
    duration = stop_time - start_time
    print(f"{duration:.10f}")
    # with open(file, 'a') as file:
    #     file.write(f"{duration:.10f}")
    return array
    

# print("Radixsort: ")
radixsort(array, XS_TABLE, int(math.log10(XS_VAR) + 1), "")