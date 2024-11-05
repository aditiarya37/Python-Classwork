class Base:
    def base(self):
        print("Base Class")
class Intermediate(Base):
    def intermediate(self):
        print("Intermediate Class")
class Derived(Intermediate):
    def derived(self):
        print("Derived Class")
obj = Derived()
obj.base()
obj.intermediate()
obj.derived()