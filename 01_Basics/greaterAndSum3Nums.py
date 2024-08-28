n1 = eval(input("Enter number 1: "))
n2 = eval(input("Enter number 2: "))
n3 = eval(input("Enter number 3: "))
print("Sum: ", n1+n2+n3)

if(n1>n2 and n1>n3):
    max = n1
elif(n2>n1 and n2>n3):
    max = n2
else:
    max = n3

print("Greatest number: ", max)