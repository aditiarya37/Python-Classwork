class Base:
    def base(self):
        print("Base Class")
class Derived1(Base):
    def derived1(self):
        print("Derived Class")
class Derived2(Base):
    def derived2(self):
        print("Derived 2 Class")
obj1 = Derived1()
obj1.base()
obj1.derived1()
obj2 = Derived2()
obj2.base()
obj2.derived2()