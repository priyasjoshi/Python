class Base1():
    def m(self):
        print("Class Base1")
class Left(Base1):
    def m(self):
        print("Class A")
class Right(Base1):
    def m(self):
        print("Class B")
class Join(Left,Right):
    pass

obj=Join ()
obj.m()

