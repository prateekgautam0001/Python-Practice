num = int(input("Enter a number: "))
if 0 <= num <= 100:
    if num % 2 == 0:
        print("Even number within range")
    else:
        print("Odd number within range")
else:
    print("Number out of range")
