"""
Задача 8: Требуется определить, можно ли от шоколадки 
размером n × m долек отломить k долек, если разрешается сделать 
один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no
"""

m = int(input('Please enter width of the chocolate bar: '))
n = int(input('Please enter length of the chocolate bar: '))
k = int(input('Please enter the amount of slices: '))

if (k < m * n) and ((k % m == 0) or (k % n == 0)):
    print('Yes')
else: print('No')
