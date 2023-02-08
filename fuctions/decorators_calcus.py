def operation(func):
    def add(a,b):
        print("I am going to add :",a+b)
        return func(a,b)
    return add
    def sub(a, b):
        print("sub:",a-b)
        return func(a,b)

@operation
def div(a,b):
    print(a/b)
div(10,4)