class A:
    def employe(self):
        self.a=input("Enter the name")
        self.b=int(input("Enter the age"))


class B:
    def salary(self):
        self.x=int(input("Enter the first month salary"))
        self.y=int(input("Enter the second month salary"))
class C(A,B):
    def employedetails(self):
        #print("{}:{}:{}:{}:{}".format("name is ",self.a,"age is ",self.b,"1st salary",self.x,"2nd salary",self.y))
         print("")
ob=C
ob.employe()
ob.salary()
ob.employedetails()


