# : a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
string = 'a a a b c a a d c d d'.split()
answer = ''
my_dict = {}
for elem in string:
    if elem in my_dict:
        answer += elem + '_' + str(my_dict[elem]) + ' '
        my_dict[elem] += 1
    else:
        answer += elem + ' '
        my_dict[elem] = 1
print(answer)

##############
import time
start = time.time()

finish = time()
print(finish - start)
