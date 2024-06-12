

import random


word_list=[]
special_char=['@','#','$','^','!']
with open("C:\\Users\\ggashaw\\Desktop\\python-a-z-15-projects\\random_pasword_generator\\wekpedia_text.txt","r") as file:
    data = file.readlines()

    for line in data:
        words=line.split()
        for item in words:
            if len(item)>5:
                word_list.append(item.capitalize())
word =random.choice(word_list)
schar =random.choice(special_char)
num =str(random.randint(10,99))
passw =word+schar+num
print(passw)
       
