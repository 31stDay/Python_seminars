"""
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""

number = int(input('Please enter three digit number:'))
digits_list = []
t_number = number

if (number > 99) and (number < 1000):
    digits_list.append(t_number % 10)
    t_number = t_number // 10
