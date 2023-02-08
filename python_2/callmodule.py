import mymodule
while True:
    opt = int(input("1.create\n2.search\n,3.remove\n4.replace\nEnter your choice"))
    if opt == 1:
        mymodule.Create()
    elif opt == 2:
        mymodule.Search()
    elif opt == 3:
        mymodule.Remove()
    elif opt == 4:
        mymodule.Replace()
    else:
        break