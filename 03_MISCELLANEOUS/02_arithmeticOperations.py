while(True):
    print()
    print("Operations are: ")
    print("1) Addition\n2) Subtraction\n3) Multiplication\n4) Divison\n5) Remainder\n6) To stop")
    choice = int(input())
    if(choice==1):
        n1 = eval(input("Enter number 1: "))
        n2 = eval(input("Enter numbe 2: "))
        print("Sum: ", n1+n2)
    elif(choice==2):
        n1 = eval(input("Enter number 1: "))
        n2 = eval(input("Enter numbe 2: "))
        print("Difference: ", n1-n2)
    elif(choice==3):
        n1 = eval(input("Enter number 1: "))
        n2 = eval(input("Enter numbe 2: "))
        print("Product: ", n1*n2)
    elif(choice==4):
        n1 = eval(input("Enter number 1: "))
        n2 = eval(input("Enter numbe 2: "))
        print("Division: ", round(n1/n2,2))
    elif(choice==5):
        n1 = eval(input("Enter number 1: "))
        n2 = eval(input("Enter numbe 2: "))
        print("Remainder: ", n1%n2)
    else:
        break