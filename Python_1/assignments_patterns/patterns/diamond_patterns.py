# n =int(input("Enter the level you want:"))
# for i in range(n):
#     print(' '*(n-i-1) + '* '*(i+1) )
# for i in range(n):
#     print(' '*(i+1) + '* '*(n-i-1))


n =int(input("Enter the level you want:"))
for i in range (n+1):
    for j in range (n-i):
        print(' ', end = ' ')
    for j in range (i):
        print('  *', end=' ')
    print()
for i in range (n+1,0,-1):
    for j in range (n-i+1):
        print(' ', end = ' ')
    for j in range (i):
        print('*  ', end=' ')
    print()
