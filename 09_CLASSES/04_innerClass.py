class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.uniobj = self.UniInfo()
    def __repr__(self):
        return "{self.name}\n{self.age}"
    class UniInfo:
        uni = "Chandigarh University"
s1 = Student("Nobita",10)
print(s1.uniobj.uni)