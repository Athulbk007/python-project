# create

l=[]
def Create():
    lst1 = int(input("enter the list"))
    for i in range(lst1):
        items = int(input("enter the items"))
        l.append(items)
        print(l)
Create()

# search
def Search():
    item = int(input("enter the item to  search"))
    if item in l:
        print("is found")
    else:
        print("not found")
    print(item)


Search()


# remove


#l=[]
def Remove():
    item = int(input("enter the item to removed"))
    if item in l:
        l.remove(item)
    else:
        print("item is not found")
    print(l)


Remove()

# replace


#l=[]
def Replace():
    old = int(input("enter the item to replace"))
    new = int(input("enter the item new item to replace"))
    for i in range(len(l)):
        if l[i] == l[old]:
            l[i] = new
    print(l)


Replace()