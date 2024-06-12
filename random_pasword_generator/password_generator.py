import random

# names=["Gashaw","Gedef","Shibabaw"]
# print(random.choice(names))
# print(random.randint(1,10))\
# print(random.random()) 
upper_char = ['A','B','C','D','E']
lower_char = ['a','b','c','d','e']
num =[1,2,3,4,5]
special_char=['@','#','$','^','!']


password =random.choice(upper_char)+random.choice(lower_char)+str(random.choice(num))+random.choice(special_char)+random.choice(upper_char)+random.choice(lower_char)+str(random.choice(num))+random.choice(special_char)
print(password)