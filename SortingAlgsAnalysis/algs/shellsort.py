import time
import sys

sys.path.insert(0, "/home/alex874565/Desktop/Facultate/Python/Sortari/samples")
from samples import *

array = reversed_table(0, XS_VAR, XL_TABLE)

def insertie_pas(array, n, h):
    for i in range(h+1, n+1):
        aux = array[i]
        j = i - h
        while j >= 1 and aux < array[j]:
            array[j+h] = array[j]
            j = j - h
        array[j+h] = aux
    return array

def shellsort(array, n, file):
    start_time = time.time()
    h = 1
    while h <= n:
        h = 3 * h + 1
    h = h//3
    array = insertie_pas(array, n, h)
    while(h != 1):
        h = h//3
        array = insertie_pas(array, n, h)[:]
    stop_time = time.time()
    duration = stop_time - start_time
    print(f"{duration:.10f}")
    # with open(file, 'a') as file:
    #    file.write(f"{duration:.10f}")
    return array

# print("Shellsort: ")
shellsort(array, XL_TABLE, "")