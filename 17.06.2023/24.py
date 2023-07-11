"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
причём кусты высажены только по окружности. Таким образом, у каждого куста есть 
ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
"""

from random import randint

def fill_bushes(number_of_bush):
    bush = [randint(1, 10) for i in range(number_of_bush)]
    return bush


def find_max_berries(bush):
    max_berries = 0
    max_i = 0
    for i in range(len(bush)):
        if bush[i] + bush[i - 1] + bush[(i + 1)% len(bush)] > max_berries:
            max_i = i + 1
            max_berries = bush[i] + bush[i - 1] + bush[(i + 1) % len(bush)]
    return max_i, max_berries
    
       
number_of_bushes = int(input('Please enter the total amount of bushes: '))

bushes = fill_bushes(number_of_bushes)
print(bushes)
print(*find_max_berries(bushes))


