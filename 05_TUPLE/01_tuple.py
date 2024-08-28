# t1 = (1,2,3,4,5)
# print(t1)
# l1 = [1]
# t1 = (1,)
# print(type(l1))
# print(type(t1))

t1 = (1,2,3,4)
t2 = (4,)
t1 += t2
print(t1)

t3 = list(t1)
t3.remove(2)
t4 = tuple(t3)
print(t4)

print(t1.count(5))
print(t1.index(2))