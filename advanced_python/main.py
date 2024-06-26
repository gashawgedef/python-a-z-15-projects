# """Walrus  Operator"""


# data = {'username':'gashawgedef','password':'gashawgedef','language':'python'}
# active = []
# def myform(data):
#     if len(username:=data['username']) >5:
#         active.append(username)
#         return active
#     else:
#         return "Inactive"
    
# print(myform(data))
# print(active)

# def process(x,y,z):
#     result = (x*y)+z
#     return result
# print(process(10,50,10))

name =input("Enter Name")
age = int(input("Enter Age:"))
# result = "My Name is %s and age is %d" %(name, age)
result = f"My Name is {name} and age is {age}"
# result = "My Name is {} and age is {}" .format(name,age)
print(result)
