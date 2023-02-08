#check if all item are same in tuple
print("\n check if all items are same in the tuples ")
tup=(1,1,1,1,1)
f=1
for i in tup:
    for j in range(i,len(tup)-1):
        if tup != tup[j+1]:
            f = 0
            break
if f == 1:
    print("are same")
else:
    print("not same")



