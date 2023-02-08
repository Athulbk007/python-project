
str='cat rat mat cat pat rat sat cat sat'
lst=str.split(' ')
print(lst)
d={}
for i in lst:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)
