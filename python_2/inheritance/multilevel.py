class A:
    def read(self):
        self.a = int(input("enter the number"))
        self.b = int(input("enter the number"))


class B(A):
    def sum(self):
        self.s = self.a + self.b
        print("sum", self.s)


class C(B):
    def Avg(self):
        print("avg", self.s / 2)


ob = C()
ob.read()
ob.sum()
ob.Avg()

#
# class A:
# #     def displayA(self):
# #         print("base")
# #
# #
# # class B(A):
# #     def displayB(self):
# #         print("intermediate class")
# #
# #
# # class C(B):
# #     def displayC(self):
# #         print("derive")
