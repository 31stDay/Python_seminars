"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X 
в массиве A[1..N]. Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. В последующих  строках записаны 
N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    3
    -> 1
"""

a = int(input('Enter the number of elements: '))
x = int(input('Enter the number you are looking for: '))

def create_list(number_of_elements):
    import random
    lst01 = [random.randint(1, 10) for i in range(number_of_elements)]
    return lst01

def how_many_times_number_occur(lst02, number):
    counter = 0
    for elem in lst02:
        if (elem == number):
            counter += 1
    return counter

lst = create_list(a)
print(lst)
print(f'Plese be informed that your number occur in the list {how_many_times_number_occur(lst, x)} times')


# rand_list=[]
# n=10
# for i in range(n):
#     rand_list.append(random.randint(3,9))
# print(rand_list)

