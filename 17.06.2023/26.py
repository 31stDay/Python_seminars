"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
"""

def raise_to_power(number, power):
      if power == 0:
            return 1
      return number * raise_to_power(number, power -1)

a = int(input('Enter your number: '))
b = int(input('Please enter to what power raise your number: '))

print(f'{a} to the power of {b} is {raise_to_power(a, b)}')
  

