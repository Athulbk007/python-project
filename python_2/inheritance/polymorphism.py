
# class A:
#     def sum (self,a):
#         print("sum",a+a)
#     def sum(self,a,b):
#         print('sum is',a+b)
#
# ob=A()
# ob.sum(10,40)

'''overloading'''
class A:
    def display(self,name=None):
        if name is None:
            print('hello')
        else:
            print('hello '+name )
ob=A()
ob.display()
ob.display('Athul')

'''overriding'''
class rectangle():
    def Area(self,l,b):
        print('Area of a rectangle is:',l*b)

class square(rectangle):
    def Area(self,l,b):
        print("Area of a square is:",l*b)

ob=square()
ob.Area(10,20)

