"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""
from random import randint

def create_list(number_of_elements):
    lst01 = [randint(1, 10) for i in range(number_of_elements)]
    return lst01
    
def sort_lists(lst01, lst02):
    set01 = sorted(set(lst01 + lst02))
    return set01

n = int(input('Please enter the number of elements in the first list: '))
m = int(input('Please enter the number of elements in the second list: '))

print(create_list(n))
print(create_list(m))
print(sort_lists(create_list(n), create_list(m)))



