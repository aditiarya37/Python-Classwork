day = str(input("Enter the day: "))
count = 0
if(day=="Monday"):
    d=1
elif(day=="Tuesday"):
    d=2
elif(day=="Wednesday"):
    d=3
elif(day=="Thursday"):
    d=4
elif(day=="Friday"):
    d=5
elif(day=="Saturday"):
    d=6
elif(day=="Sunday"):
    d=7
for i in range(d,367,7):
    count += 1
print(count)