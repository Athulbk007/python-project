"""program to print all number in a range divible by given number"""
lower=int(input("enter lower range limit:"))
upper=int(input("enter upper range limit:"))
n = int(input("enter the number to be divided by:"))
# the remainder of the number divided by i is equal to 0, i is printed.
for i in range(lower, upper+1):
    if (i % n ==0):
        print(i)
