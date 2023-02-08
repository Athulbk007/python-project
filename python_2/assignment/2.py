#pyramid of harizondal number tables

rows=7
for i in range(1,rows+1):  #for rows
    for j in range(1,i+1): #for columns
        print(i*j,end=' ')
    print()