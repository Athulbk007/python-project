n=int(input("Enter a number:"))
for i in range(n):
    for s in range(i):
        print(" ", end="")
    for j in range(n-i):
        print("* ", end="")
    print()
for i in range(n-1,-1,-1):
    for s in range(i):
        print(" ", end="")
    for j in range(n-i):
        print("* ", end="")
    print()












