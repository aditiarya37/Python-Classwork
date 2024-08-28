def add(n1, n2):
    return n1+n2
def sub(n1, n2):
    return n1-n2
def mul(n1, n2):
    return n1*n2
def division(n1, n2):
    return round(n1/n2,2)
def remainder(n1, n2):
    return n1%n2
n1 = eval(input("Enter number 1: "))
n2 = eval(input("Enter number 2: "))
print("Sum: ", add(n1,n2))
print("Difference: ", sub(n1,n2))
print("Product: ", mul(n1,n2))
print("Division: ", division(n1,n2))
print("Remainder: ", remainder(n1,n2))