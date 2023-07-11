"""
Задача №51. 
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.
Ввод: Вывод:
values = [0, 2, 10, 6] same
if same_by(lambda x: x % 2, values):
print(‘same’)
else:
print(‘different’)
"""

values = [0, 2, 10, 6] same
if same_by(lambda x: x % 2, values):
print(‘same’)
else:
print(‘different’)
      




#       values = [0, 2, 10, 6] 
# def same_by(characteristic, objects):
#     if not objects:
#        return True
#     characteristic_etalon = characteristic(objects[1])
#     for i in objects:
#         if characteristic(objects[i]) == characteristic_etalon:
#            return True
#     else: return 'Different'
# print(same_by(lambda x: x % 2, values))



# def same_by (func, array):
#     result_list = []
#     for i in range(len(array)):
#         result_list.append(func(array[i]))
#     result_set=set(result_list) 
#     if len(result_set)>1:
#         return False
#     else:
#         return True