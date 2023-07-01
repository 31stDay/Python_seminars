"""
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""

number = int(input('Input number: '))

def isSimple(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print(isSimple(number))