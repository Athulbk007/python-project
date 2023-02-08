n = int(input("Enter the number :"))
count = 0
i = 2
while i< n:
    if n % i == 0:
        count = 1
        print(n,"is not a prime number")
    i = i + 1
if count ==0:
    print(n,"is a prime number")
