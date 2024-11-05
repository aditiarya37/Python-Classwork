class Base1:
    def base1(self):
        print("Base 1 Class")
    def show():
        print(5)
class Base2:
    def base2(self):
        print("Base 2 Class")
    def show():
        print(10)
class Derived(Base2,Base1):
    def derived(self):
        print("Derived Class")
obj = Derived()
obj.base1()
obj.base2()
obj.derived()
obj.show()