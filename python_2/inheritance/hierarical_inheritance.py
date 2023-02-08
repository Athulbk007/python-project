class A:
    def read(self):
        self.a = int(input("enter the number"))
        self.b = int(input("enter the number"))


class B(A):
    def Sum(self):
        self.s = self.a + self.b
        print("sum", self.s)


class C(A):
    def Avg(self):
        print("avg", (self.a+self.b)/2)


class D(A):
    def product(self):
        print("product",self.a*self.b)

ob1=B()
ob1.read()
ob1.Sum()

ob2=C()
ob1.read()
ob2.Avg()


ob3=D()
ob1.read()
ob3.product()





