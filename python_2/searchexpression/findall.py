#find all
import re
# str='rose is beatiful and colorful color'
# # s=re.findall('ful',str)
# # print(s)
#
#
# d='cat rat mat pat'
# s=re.findall('[sc]a',d)
# print(s)
#
#^
# d='cat rat mat pat'
# s=re.findall('[^sc]',d)
# print(s)

#
# d='cat mat rat pat sat 99988 9999'
# a=re.findall('\d{3}',d)
# print(a)


d='cat mat rat pat sat 99988 9999'
a=re.findall('\d{1,3}',d)#range
print(a)

d='cat mat rat pat sat 99988 9999'
a=re.findall(r'\b\d{1,3}\b',d)#\
print(a)



