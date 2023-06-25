"""
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""

number = int(input('Please enter three digit number:'))
digits_list = []
t_number = number
sum = 0
if (number > 99) and (number < 1000):
    while (t_number > 0):
        digits_list.append(t_number % 10)
        t_number = t_number // 10
    for elem in digits_list:
        sum += elem
    print(f'{number} -> {sum}({digits_list[:]})')
else: print('You\'ve enter the wrong number!')
        
