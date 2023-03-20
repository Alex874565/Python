import sys
from time import time
import math
import threading 
import resource, sys

resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.path.insert(0, "/home/alex874565/Desktop/Facultate/Python/SortingAlgsAnalysis/algs")
sys.path.insert(0, "/home/alex874565/Desktop/Facultate/Python/SortingAlgsAnalysis/samples")

sys.setrecursionlimit(1000000)

from countingsort import *
from insertie import *
from mergesort import *
from quicksort import *
from radixsort import *
from selectie import *
from shakersort import *
from shellsort import *
from interschimbare import *
from samples import *

threading.stack_size(0x2000000)

algs = [insertie, selectie, interschimbare, mergesort, quicksort, countingsort, radixsort, shellsort, shakersort]

FILE = ""
FILE2 = ""


y = ['']
for i in range(XL_TABLE):
    y.append(0)

for table_type in table_types:
     with open(FILE, 'a') as f:
         f.write(f"\n\nTABLE_TYPE: {table_type.__name__}")
     for table_size in table_sizes[:-1]:
         with open(FILE, 'a') as f:
             f.write(f"\n\nTABLE_SIZE: 10^{int(math.log10(table_size))}")
         for index in range(1, len(var_sizes)):
             var_size = var_sizes[index] 
             if table_size <= var_size:
                 array = table_type(var_sizes[index - 1], var_size, table_size)
                 t = array[:]
                 with open(FILE, 'a') as f:
                     f.write(f"\n\nVAR_SIZE: 10^{int(math.log10(var_size))}")
               
                     f.write("\n\nInsertie:\n")
                 insertie(t, table_size, FILE)
                 t = array[:]
                 with open(FILE, 'a') as f:
                     f.write("\n\nSelectie:\n")
                 selectie(t, table_size, FILE)
                 t = array[:]
                 with open(FILE, 'a') as f:
                     f.write("\n\nInterschimbare:\n")
                 interschimbare(t, table_size + 1, FILE)
                 t = array[:]
                 with open(FILE, 'a') as f:
                     f.write("\n\nMergesort:\n")
                     start_time = time.time()
                     mergesort(t, 1, table_size)
                     stop_time = time.time()
                     duration = stop_time - start_time
                     f.write(f"{duration:.10f}")
                     t = array[:]

                     f.write("\n\nQuicksort:\n")
                     start_time = time.time()
                     quicksort(t, 1, table_size)
                     stop_time = time.time()
                     duration = stop_time - start_time
                     f.write(f"{duration:.10f}")
                     t = array[:]

                     f.write("\n\nCountingsort:\n")
                 if var_size < M_VAR:
                     countingsort(t, table_size, FILE)
                     t = array[:]

                 with open(FILE, 'a') as f:
                     f.write("\n\nRadixsort:\n")
                 radixsort(t, table_size, int(math.log10(var_size)+1), FILE)
                 t = array[:]

                 with open(FILE, 'a') as f:
                     f.write("\n\nShellsort:\n")
                 shellsort(t, table_size, FILE)
                 t = array[:]

                 with open(FILE, 'a') as f:
                     f.write("\n\nShakersort:\n")
                 shakersort(t, table_size, FILE)
                 t = array[:]