
from functools import reduce
lst = [5,10,15,20,25]
# x = 0
# def sum(lst):
#     global x
#     for item in lst:
#         x +=item
#     return x
    
# print(sum(lst))
print(reduce(lambda x,y:x+y,lst))
