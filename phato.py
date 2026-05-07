import itertools
import random

sample_space = list(itertools.product(['H', 'T'], repeat=2))
print("Sample Space:", sample_space)

print('*' * 50)

sample_space_Q2 = [1, 2, 3, 4, 5, 6]
P_even = len( [2,4,6] ) / len(sample_space_Q2)
print("\nSample Space:", sample_space_Q2)
print("P(rolling even) =", P_even)

print('*' * 50)

sample_space_Q3 = ['R1', 'R2', 'B']
P_each = {outcome: 1/3 for outcome in sample_space_Q3}
print("\nQ3 Sample Space & Probabilities:", P_each,'\n')

print('*' * 50)
















# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fact(x - 1)
# print(fact(5))

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# list_1 = [a,b,c,d,e]
# odd = 0
# i = 0
# for i in range(0,5):
#         if list_1[i] % 2 != 0:
#             odd += list_1[i]    
                
# print(odd)




