def sum(a,b):
    return a+b
print(sum(20,30))
#lambda
#syntax:argument:expression
add=lambda a,b:a+b
print(add(50,60))

largest = lambda a, b: a if a > b else b
print(largest(100, 500))

# #filter
#l=[10,2,3,4,55,6,8]
# list1=list(filter(lambda x:x%2==0,l))
# print(list1)

#map
# l=[10,2,3,4,55,6,8]
# list2=list(map(lambda x:x%2==0,l))
# print(list2)


#reduce
# from functools import reduce
# l1=[2,3,4,5,6]
# product=reduce(lambda x,y:x*y,l1)
# print(product)



#list comperhension

# l1=[x+3 for x in [2,3,4,]]
# print(l1)

#even numbers
# l2=[i for i in range(25) if i%2==0]
# print(l2)

#vowels of a string

# l3=[i for i in 'umbrella' if i in ['a','e','i','o','u']]
# print(l3)

#split
# str ="how are you"
# words=str.split( )
# letter=[i[0] for i in words]
# print(letter)
# #print(words)

colors=['red','white','green','pink']
l=[i for i in colors if "e" in i ]
print(l)

colors=['red','white','green','pink']
newlist=[i for i in colors if i!="green"]
print(newlist)

#uppercase
colors=['red','white','green','pink']
newlist=[i.upper() for i in colors ]
print(newlist)



colors=['red','white','green','pink']
newlist=['hello' for i in colors]
print(newlist)

colors=['red','white','green','pink']
newlist=[i if i!='pink' else 'blue' for i in colors]
print(newlist)








































