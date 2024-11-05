class Base1:
    def base1(self):
        print("Base 1 Class")
class Base2:
    def base2(self):
        print("Base 2 Class")
class Intermediate(Base1):
    def intermediate(self):
        print("Intermediate Class")
class Derived1(Base1, Base2):
    def derived1(self):
        print("Derived 1 Class")
class Derived2(Intermediate):
    def derived2(self):
        print("Derived 2 Class")
obj1 = Derived1()
obj1.base1()
obj1.base2()
obj1.derived1()
obj2 = Derived2()
obj2.base1()
obj2.intermediate()
obj2.derived2()