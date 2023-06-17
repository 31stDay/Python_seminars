"""
Задача №3. 
В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32
"""

firstClass = int(input('Enter A: '))
secondClass = int(input('Enter B: '))
thirdClass = int(input('Enter C: '))

desksAmount = ((firstClass // 2) + (firstClass % 2))+ ((secondClass // 2) + (secondClass % 2)) + ((thirdClass // 2) + (thirdClass % 2))
print(desksAmount)