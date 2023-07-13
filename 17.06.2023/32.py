"""
Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону (т.е. 
не меньше заданного минимума и не больше заданного максимума)
"""
from random import randint
list01 = [randint(1, 200) for i in range(10)]
print(list01)
maximum = 100
minimum = 1
list02 = []
for i in range(len(list01)):
    if (minimum < list01[i] < maximum):
        list02.append(i)

print('List of indexes of elements less then max and greater than min: ') 
print(list02)




