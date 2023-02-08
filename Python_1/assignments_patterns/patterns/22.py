#square pattern
# n=4
# for i in range(0,n):
#     for j in  range(0,n):
#         print("*",end=" ")
#     print()

#hollow pattern
# n=4
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#left tri pattern

# n=5
# for i in range(1,n+1):
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()

#right tri pattern
n=5
for i in range(1,n-1):
    for k in range(1,i-1):
        print("*",end=" ")
    print()