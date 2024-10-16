class average:
    name = "XYZ"
    age = "eighteen"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    # def avg(self):
    #     return round((self.m1+self.m2+self.m3)/3,2)
    @classmethod
    def clsfunc(cls):
        return cls.name + " " + cls.age
    @staticmethod
    def staticmethod():
        print("Static function")
ans = average(89,93,96)
print(average.clsfunc())
average.staticmethod()