# class student:
#     name = "Nobita"
#     age = 10
# s1 = student()
# print(s1.name)
# print(s1.age)

class student:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    # def __str__ (self):
    #     # return self.name + " " + str(self.age)
    #     return f"{self.name} {self.age}"
    def __repr__(self):
        return f"{self.name} {self.age}"
s1 = student("Nobita",10)
print(s1)
# print(s1.name)
# print(s1.age)