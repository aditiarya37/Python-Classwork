def binarySearch(list,s,e,key):
    if s>e:
        return -1
    mid = s+(e-s)//2
    if list[mid]==key:
        return mid
    elif list[mid]<key:
        return binarySearch(list,mid+1,e,key)
    else:
        return binarySearch(list,s,mid-1,key)
list = [65,12,53,31,75]
list.sort()
x = int(input("Enter the key: "))
ans = binarySearch(list,0,len(list)-1,x)
print("The sorted list is: ", list)
print("Element fount at:", ans)