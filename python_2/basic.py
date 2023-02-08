# swapping
# a,b=int(input("enter the first number")),int (input("enter the second number"))
# a,b=b,a
# print("a=",a)
# print("b=",b)


# write a prg given num is positve or neg or equal

# a=int(input("enter the number:"))
# if a <0:
#     print("the num is negative")
# elif a>0:
#     print("the num is positive:")
# else:
#     print("the num is equal")


# largest of three number in nested if

# a=int(input("Enter the number a:"))
# b=int(input("Enter the number b:"))
# c=int(input("Enter the number c:"))
#
# if a>b:
#     if a>c:
#         print("a is the largest number",a)
#     else:
#         print("c is the largest number",c)
# elif b>c:
#     print("b is the largest number",b)
# else:
#     print("c is the largest number",c)
#


# reverse of a number using while
# n=example
# rev=0
# p=1
# s=0
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     p=p*r#product
#     s=s+r#sum
#     n=n//10
#
# print("the reverse number",rev)
# print("the product number",p)
# print("the sum number",s)


# to print fibannoci series or range method

# n=int(input("enter the number :"))
# a,b=0,1
# print('fibanocci series')
# print(a)
# print(b)
# for i in range(3,n+1):
#     c=a+b
#     print(c)
#     a,b=b,c

# prime number
# n = int(input("enter the number"))
# f = 0
# # n=5----5%1=0,5%2=1,5%3=2,5%4=1,5%5=0
# if n == 1:
#     print("not defined")
# else:
#     for i in range(1, n + 1):  # 1---n
#         if n % i == 0:
#             f = f + 1  # 2
#     if f == 2:
#         print("prime number")
#     else:
#         print("not prime")

# break
# l=[10,20,30,100,50,40]
# for x in l:
#     print(x)
#     if x==100:
#         break

# continue
# for x in l:
#     if x==100:
#         continue
#     print(x)

# reverse sorting

# l=[10,20,30,100,50,40]
# l.sort(reverse=True)
# print(l)


# add value in empty list
# list1 = []
# num = int(input("enter the number of elements in list:"))
# for i in range(num):
#     item=int(input("enter the item:"))
#     list1.append(item)
# print(list1)
#
#
#dictionary

dict1 = {"name":"Athul","age":22,"course":"python","address":"malappuram"}
#print(dict1)
dict1.update({"name":"qwer"})
print(dict1)

d={}
number = int(input("enter the elements in the dictionary"))
for i in range(number):
    key=int(input("enter the key"))
    values=input("enter the values")
    d.update({key:values})
print(d)

d={1:"red",2:"blue"}
for i in d.keys():
    print(i)


d={1:"red",2:"blue"}
for i in d.values():
    print(i)

for i,j in d.items():
    print(i,j)

x=d.get(2)
print(x)

#set
# s={10,20,70,50}
# print(s)
# for i in s:
#     print(i)

#fuctions
