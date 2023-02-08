def programing():

    def python():
        nonlocal name
        name = "sreejesh"

    def mean_stack():
        global name
        name = "pavan kumar"
    mean_stack()

    def flutter():
        name = "shihab"

    name = "sanjay"

    python()
    print("coder is :" + name)
programing()
print(name)
