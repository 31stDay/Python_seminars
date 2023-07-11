from os import system
from random import randint
import time


print(
    "Какую задачу смотрим: введите порядковый номер задачи или введите 0 чтобы посмотреть все"
)
task_number = int(input("Укажите порядковый номер задачи, которую будем смотреть "))


def get_list_from_user(number):
    array = []
    for i in range(number):
        array.append(int(input("Введите число ")))
    return array


def get_list(number, min_value, max_value):
    array = []
    for i in range(number):
        i = int(randint(min_value, max_value))
        array.append(i)
    return array


if task_number == 1 or task_number == 0:
    print(
        "Задача №39. Решение в группах Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива Ввод: Вывод: 7 3 3 2 12 3 1 3 4 2 4 12 6 4 15 43 1 15 1 (каждое число вводится с новой строки)"
    )
    start = time.time()
    list_task_39a = get_list_from_user(
        int(input("Укажите количество элементов в списке "))
    )
    print("Первый список ", list_task_39a)
    list_task_39b = get_list_from_user(
        int(input("Укажите количество элементов в списке "))
    )
    print("Второй список ", list_task_39b)
    for i in list_task_39a:
        if i not in list_task_39b:
            print(i)

    finish = time.time()
    print("Время работы программы ", finish - start)
    input("Нажмите Enter что бы продолжить ")
    system("cls")

if task_number == 2 or task_number == 0:
    print(
        "Задача №41. Решение в группах Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел. Ввод: Ввод: 5 5 1 2 3 4 5 1 5 1 5 1 Вывод: Вывод: 0 2 "
    )
    list_task_41 = get_list(
        int(input("Укажите количество чисел в списке ")),
        int(input("Укажите минимальное значение ")),
        int(input("Укажите максимальное значение ")),
    )
    print("Получен следующий список ", list_task_41)
    serched_number = int(input("Введите искомое число "))
    count_serched_number_req = 0
    for i in range(len(list_task_41)):
        if list_task_41[i] == serched_number:
            if (
                list_task_41[i - 1] < serched_number
                and list_task_41[i + 1] < serched_number
            ):
                count_serched_number_req += 1
    print('Количество элементов удовлетворяюих условию = ', count_serched_number_req)





    ############################
    f = open('my_filr')


