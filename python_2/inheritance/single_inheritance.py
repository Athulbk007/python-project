# class A:
#     def displayA(self):
#         print("base method")
# class B(A):
#     def displayB(self):
#         print("derive method")
# ob=B()
# ob.displayA()
# ob.displayB()

class A:
    def read(self):
        self.a=int(input("enter the number"))
        self.b=int(input("enter the number"))

class B(A):
    def sum(self):
        print("sum",self.a+self.b)

ob=B()
ob.read()
ob.sum()