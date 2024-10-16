def binarySearch(list, x):
    s = 0
    e = len(list)-1
    while s<=e:
        mid = s+(e-s)//2
        if list[mid]==x:
            return mid
        elif list[mid]<x:
            s = mid+1
        else:
            e = mid-1
    return -1
list = [65,12,53,31,75]
list.sort()
x = int(input("Enter the key: "))
ans = binarySearch(list,x)
print("The sorted list is: ", list)
print("Element fount at:", ans)
