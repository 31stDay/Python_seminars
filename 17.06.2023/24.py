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


number_of_bushes = int(input('Please enter the total amount of bushes: '))

def fill_bushes(n):
    import random
    bushes01 = {}
    for key in range(n):
        bushes01[key] = int(random.randint(10, 90))
    return bushes01

def find_max_berries(bushes02):
    for key in bushes02:
        berries_from_three_bushes = bushes02[key] + bushes02[key + 1] + bushes02[key - 1]
       

bushes = fill_bushes(number_of_bushes)
print(f'{bushes}')


####
for i in range(number_of_bushes):
        summ_yield = sum([yield_list[i] + yield_list[i - 1] + yield_list[(i + 1) % number_of_bushes]])
        if summ_yield > max_summ_yield:
            max_summ_yield = summ_yield
######################
quantity_bush = int(input("Введите кол-во кустов на грядке:\n"))
list_1 = [randint(1, 15) for i in range(quantity_bush)]
print(f"Кол-во ягод на каждом кусте {list_1}")
count = 0
max_quantity_berries = 0
for i in range(-1, quantity_bush - 1):
    count = list_1[i - 1] + list_1[i] + list_1[i + 1]
    print(count)
    if max_quantity_berries < count:
        max_quantity_berries = count
    count = 0
print(f"Максимальное число ягод = {max_quantity_berries}")
############################


