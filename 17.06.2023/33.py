"""
Задача №33. Общее обсуждение
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""


n = int(input('Enter number of grades: '))
string = input('Enter grades separated by a space: ')
lst = [int(i) for i in string.split()]

def swap_grades(list01):
    maxim = list01[0]
    minim = list01[0]
    for i in range(1, n):
        if(list01[i] > maxim):
            maxim = list01[i]
            i_maxim = i
        else:
            if(list01[i] < minim):
                minim = list01[i]

    #list01[i_maxim] =  list01[i_minim]
    list01[i_maxim] = minim
    return list01 
    
print(swap_grades(lst))

"""
    arr = [1, 3, 3, 3, 4]

def find(array):
    maximum = max(array)
    minimum = min(array)
        
    for i in range(len(array)):
        if array[i] == maximum:
            array[i] = minimum
    
    return array

print(arr)
print(find(arr))
    """

    

