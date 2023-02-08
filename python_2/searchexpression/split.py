#split()
import re

str='class will start at 10am'
a=re.split(' ',str)
print(a)

str='class will start at 10am'
a=re.split('s',str)
print(a)

str='class will start at 10am'
a=re.split('s',str,2)
print(a)


