import time
import sys

sys.path.insert(0, "/home/alex874565/Desktop/Facultate/Python/Sortari/samples")
from samples import *

array = ordered_table(0, VAR_SIZE, TABLE_SIZE)

def interschimbare(array, n, file):
    start_time = time.time()
    t = n - 1
    while t > 1:
        m = t
        t = 0
        for j in range(1, m):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                t = j
    stop_time = time.time()
    duration = stop_time - start_time
    print(f"{duration:.10f}")
    #with open(file, 'a') as file:
    #    file.write(f"{duration:.10f}")
    return array

# print("Interschimbare: ")
interschimbare(array, TABLE_SIZE + 1, "")