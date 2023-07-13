"""
Задача 30:  Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""

first_element = int(input('Enter your number: '))
number_of_elements = int(input('Enter the number of elements: '))
step = int(input('Enter the difference: '))

list01 = [first_element + i * step for i in range(number_of_elements)]
print(list01)