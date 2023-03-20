import time
import sys

sys.path.insert(0, "/home/alex874565/Desktop/Facultate/Python/Sortari/samples")
from samples import *

array = TABLE_TYPE(0, VAR_SIZE, TABLE_SIZE)

def selectie(array, n, file):
    start_time = time.time()
    for i in range(1, n):
        k = i
        for j in range(i+1, n):
            if array[k] > array[j]:
                k = j
        if k != i:
            array[i], array[k] = array[k], array[i]
    stop_time = time.time()
    duration = stop_time - start_time
    print(f"{duration:.10f}")
    with open(file, 'a') as file:
        file.write(f"{duration:.10f}")
    return array

# print("Selectie: ")
# selectie(array, TABLE_SIZE)