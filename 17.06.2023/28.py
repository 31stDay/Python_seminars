# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

def sum_rec(a, b):
    if a == 0:
        return b
    else:
        return sum_rec(a - 1, b + 1)
    
a = int(input('Enter your number: '))
b = int(input('Please your second number: '))

print(f'{a} plus {b} is equal {sum_rec(a, b)}')  
