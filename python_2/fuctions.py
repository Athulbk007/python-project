# def sum():
#     a=10
#     b=20
#     s=a+b
#     return s
# sum()
# print("sum is ",sum())
#
# def sum(a,b):
#     s=a+b
#     return s
# s=sum(20,40)
# print(s)
# print("sum is ",sum(100,500))


# write a prg of a factorial of a  number using function with return type and paramaters
#
# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
# f=fact(5)
# print("factorial of number",f)
#
#
# #argument
# def color(*args):
#     print(args[0])
#     for i in args:
# #         print(i)
# def color(x,*args):
#     print("normal argument",args[0])
#     for i in args:
#         print(i)
#
#
# color("yellow", "red", "white")


# KEYWORD ARGUMENTS

# def stud(str1, str2, str3):
#     print("first", str1)
#     print("second", str2)
#     print("third", str3)
#
#
# stud(str2="anu", str1="kiran", str3="baba")
#


# def student(**kwargs):
#     for i,j in kwargs.items():
#         print("%s=>%s"%(i,j))
#
#
# student(str1="anu",str3="haha",str2="jack")

# companing simple,arbitary,keyword

# def student(x,*args,**kwargs):
#     print("simple arguments",x)
#     for j in args:
#         print(j)
#     for i,j in kwargs.items():
#         print("%s=>%s"%(i,j))
#
#
# student("athul","varun","dawan",str1="anu",str3="haha",str2="jack")


# default parameters

# def display(country="india"):
#     print("i am from",country)
# display()
# display("america")


# list

# def dis(ls):
#     for i in ls:
#         print(i)
# dis([10,20,40])



# create

l=[]
def Create():
    lst1 = int(input("enter the list"))
    for i in range(lst1):
        items = int(input("enter the items"))
        l.append(items)
        print(l)
create()

# search
def Search():
    item = int(input("enter the item to  search"))
    if item in l:
        print("is found")
    else:
        print("not found")
    print(item)


Search()


# remove
l = []


def Remove():
    item = int(input("enter the item to removed"))
    if item in l:
        l.remove(item)
    else:
        print("item is not found")
    print(l)


Remove()

# replace


l=[]
def Replace():
    old = int(input("enter the item to replace"))
    new = int(input("enter the item new item to replace"))
    for i in range(len(l)):
        if l[i] == l[old]:
            l[i] = new
    print(l)


Replace()


while True:
    opt = int(input("1.create\n2.search\n,3.remove\n4.replace\nEnter your choice"))
    if opt == 1:
        create()
    elif opt == 2:
        search()
    elif opt == 3:
        remove()
    elif opt == 4:
        replace()
    else:
        break