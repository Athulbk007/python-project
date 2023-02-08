#factorial
class Fact:
    def fact(s1,x):
        if x==1:
            return 1
        else:
            return x*Fact.fact(s1,x-1)
obj=Fact()
x=int(input("enter the number:"))
f=obj.fact(x)
print("factorial is:",f)
