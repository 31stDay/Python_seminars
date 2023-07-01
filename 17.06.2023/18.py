"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент 
к заданному числу X. Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5
"""

def create_list(number_of_elements):
    import random
    lst01 = [random.randint(1, 10) for i in range(number_of_elements)]
    return lst01

def find_nearest_number(lst02, number):
    nearest_number = lst02[0]
    min_diff = lst02[0] - number
    if(min_diff < 0):
        min_diff = min_diff * (-1)

    for elem in lst02:
        diff = elem - number
        if (diff < 0):
            diff = diff *(-1)
        if(diff < min_diff):
            nearest_number = elem
    return nearest_number
    

a = int(input('Enter the number of elements: '))
x = int(input('Enter your number: '))

lst = create_list(a)
print(lst)
print(f'Plese be informed that the nearest number to your number {x} is {find_nearest_number(lst, x)} ')
