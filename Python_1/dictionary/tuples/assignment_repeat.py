#Let’s google the pineapple

str ="Let’s google the pineapple"
print(str)
str1= str.split()
str2= []
for i in str1:
    l =" "
    for j in i:
        if j in l:
            continue
        else:
            l=l+j
            str2.append(l)
    print(''.join(l),end="")

