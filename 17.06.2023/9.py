"""
Задача №9. Решение в группах
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120
"""

number = int(input('Введите число: '))
factorial = number

for i in range(2, number):
    factorial = factorial * i # 5 * 2 * 3 * 4

print(factorial)

"""
number = int(input("Введите число "))
    factorial_n = 1
    step = 1
    while step <= number:
        factorial_n *= step
        step += 1

    print(factorial_n)
"""