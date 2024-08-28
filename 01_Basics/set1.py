while True:
    print("Enter the shape:")
    print("1) Circle\n 2) Square\n 3) Triangle\n 4) To exit")
    shape = int(input())
    if shape==1:
        rad = float(input("Enter the radius of the circle: "))
        ans = 3.14*rad*rad
        print("Area of the circle: ", ans)
    elif shape==2:
        side = float(input("Enter the side of the square: "))
        ans = side*side
        print("Area of the square: ", ans)
    elif shape==3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        ans= 0.5*base*height
        print("Area of the triangle: ", ans)
    else:
        print("You have finished.")
        break
