"""
Задача №15. Решение в группах
15. Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9
"""

n = int(input('количество арбузов '))


for i in range(1, n + 1):
    watermelon = int(input('масса арбуза: '))
    max_watermelon = min_watermelon = watermelon

    if (max_watermelon < watermelon):
        max_watermelon = watermelon
    if (min_watermelon > watermelon): 
        min_watermelon = watermelon

print( min_watermelon, max_watermelon)

"""
import random

N = int(input("Введите кол-во арбузов: "))
array = []

for i in range(N):
    i = random.randint(2, 10)
    array.append(i)

print(max(array), min(array))
print(array)
"""
