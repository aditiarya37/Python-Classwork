class Base1:
    def base1(self):
        print("Base 1 Class")
class Base2:
    def base2(self):
        print("Base 2 Class")
class Derived(Base1, Base2):
    def derived(self):
        print("Derived Class")
obj = Derived()
obj.base1()
obj.base2()
obj.derived()