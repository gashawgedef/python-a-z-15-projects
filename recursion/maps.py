

lists = [5,10,20,25,50]

# sqr_lst =[]
# def square(lst):
#     for item in lst:
#         sqr_lst.append(item**2)
#     return sqr_lst
# print(square(lists))
# def square(num):
#     return num**2
# print(list(map(square,lists)))

print(list(map(lambda num: num**2, lists)))