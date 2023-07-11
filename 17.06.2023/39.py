"""
Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод: Вывод:
7 3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1 (каждое число вводится с новой строки)
"""
def create_list(number_of_elements):
    import random
    lst = [random.randint(1, 10) for i in range(number_of_elements)]
    return lst

def sort_elements(list01, list02):



n = int(input('Enter the number of elements in the first array: '))
m = int(input('Enter the number of elements in the second array: '))
lst01 = create_list(n)
lst02 = create_list(m)



#################
# list_task_39a = get_list_from_user(
#         int(input("Укажите количество элементов в списке "))
#     )
#     print("Первый список ", list_task_39a)
#     list_task_39b = get_list_from_user(
#         int(input("Укажите количество элементов в списке "))
#     )
#     print("Второй список ", list_task_39b)
#     for i in list_task_39a:
#         if i not in list_task_39b:
#             print(i)

