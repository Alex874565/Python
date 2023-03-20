import time
import sys

sys.path.insert(0, "/home/alex874565/Desktop/Facultate/Python/Sortari/samples")
from samples import *

table = TABLE_TYPE(0, VAR_SIZE, TABLE_SIZE)

def insertie(array, n, file):
    start_time = time.time()
    for i in range(2, n):
        aux = array[i]
        j = i-1
        while j >= 1 and aux < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = aux
    stop_time = time.time()
    duration = stop_time - start_time
    print(f"{duration:.10f}")
    with open(file, 'a') as file:
        file.write(f"{duration:.10f}")
    return array

# print("Insertie: ")
insertie(table, TABLE_SIZE)

