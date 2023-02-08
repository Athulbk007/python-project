num = int(input("Enter the number"))
for i in range(0,num):
    print(" " *(num-i)+"*",end = " ")
    if i != 0 :
        print(" "*(2*i)+"*",end=" ")
    print()
for i in range(num,-1,-1):
        print(" "*(num-i) + "*", end=" ")
        if i != 0:
            print(" "* (2*i) + "*", end=" ")
        print()