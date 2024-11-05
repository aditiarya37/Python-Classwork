class Base:
    def base(self):
        print("Base Class")
class Derived(Base):
    def derived(self):
        print("Derived Class")
# obj1 = Base()
obj2 = Derived()
obj2.base()
obj2.derived()