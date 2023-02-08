n = int(input("Enter the number to be reversed :"))
i = 0
rev = 0
while n > 0:
    rev = rev * 10 +n%10
    n = n //10
print("Reverse number is : ",rev)
