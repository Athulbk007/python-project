# import re
# input=("rose and jasmine are flowers")
# a=re.sub(' ','*',input)
# print(a)
# b=re.sub(' ','*',input,2)
# print(b)


import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
        print("Valid email")
    else:
        print("Invalid email")


isValid("qwertyu@gmail.in")
isValid("123456@yaddfgqwerty")
