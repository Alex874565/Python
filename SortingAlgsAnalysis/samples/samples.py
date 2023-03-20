import random

XS_TABLE = pow(10, 2)
S_TABLE = pow(10,3)
M_TABLE = pow(10,4)
L_TABLE = pow(10,5)
XL_TABLE = pow(10,6)

XS_VAR = pow(10, 2)
S_VAR = pow(10,6)
M_VAR = pow(10, 20)
L_VAR = pow(10, 50)
XL_VAR = pow(10, 100)

def ordered_table(min, max, size):
    table = ['']
    for i in range(size):
        table.append(i + max - size)
    return table

def semiordered_table(min, max, size):
    table = ['']
    step = 1
    i = 0
    while i < size:
        step = random.randint(1, 10)
        value = random.randint(min, max)
        for j in range(step):
            table.append(value + j)
        i += step
    return table

def reversed_table(min, max, size):
    table = ['']
    for i in range(size):
        table.append(max - i)
    return table

def shuffled_table(min, max, size):
    table = ['']
    for i in range(size):
        table.append(random.randint(min, max))
    return table

table_sizes = [XS_TABLE, S_TABLE, M_TABLE, L_TABLE, XL_TABLE]
var_sizes = [0, XS_VAR, S_VAR, M_VAR, L_VAR, XL_VAR]
table_types = [ordered_table, reversed_table, semiordered_table, shuffled_table]