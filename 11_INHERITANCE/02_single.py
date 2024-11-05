class Base:
    def base(self):
        print("Base Class")
class Derived(Base):
    def derived(self):
        print("Derived Class")
obj = Derived()
obj.base()
obj.derived()