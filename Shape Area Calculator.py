shape = input("Enter shape (circle, square, rectangle): ").lower()
match shape:
    case "circle":
        r = float(input("Radius: "))
        print("Area:", 3.14 * r * r)
    case "square":
        a = float(input("Side: "))
        print("Area:", a * a)
    case "rectangle":
        l = float(input("Length: "))
        w = float(input("Width: "))
        print("Area:", l * w)
    case _:
        print("Invalid shape")
