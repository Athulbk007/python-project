choice = input("Enter the choice : +,-*,/")
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2st number: "))
if choice=='+':
    print("sum is ",a+b)
elif choice=="-":
    c = a-b
    print(c,"Difference is ")
elif choice=="*":
    print("multiply is ",a*b)
elif choice=="/":
    print("division is ",a/b)
else:
    print("invalid")