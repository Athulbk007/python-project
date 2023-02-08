import re
# str='class will start at 10am'
# a=re.search('\s' ,str)
# print(a)
# print(a.start())
#
# b=re.search('\d' ,str)#\dstop
# print(b)
# print(b.start())
#
# c=re.search('python',str)
# print(c)


str='class will start at 10am'
a=re.search('^class.*10am$',str)#end
print(a)
if a:
    print("find")
else:
    print('not find')
