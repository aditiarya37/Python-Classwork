def linearSearch(list,x):
    for i,val in enumerate(list):
        if val == x:
            return i
    return -1
list = [1,2,3,4,5]
x = int(input("Enter the key: "))
ans = linearSearch(list,x)
print("Element found at:", ans)
