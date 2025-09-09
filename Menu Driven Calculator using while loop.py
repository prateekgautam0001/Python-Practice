while True:
    print("\n1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit")
    choice = input("Choose: ")
    if choice == '5':
        break
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if choice == '1':
        print("Result:", a + b)
    elif choice == '2':
        print("Result:", a - b)
    elif choice == '3':
        print("Result:", a * b)
    elif choice == '4':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Division by zero")
