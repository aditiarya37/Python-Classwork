# Elements of the sets are unordered, unlike lists and tuples.
s1 = set((1,2,3,4,5))
# s1.add(6)
# print(s1)
# s2 = {11,12,13}
# s1.update(s2)
# print(s1)
# l1 = [11,12,13]
# s1.update(l1)
# print(s1)
s1.remove(6) # Gives error if the element is not present.
print(s1)
s1.discard(6)
print(s1)