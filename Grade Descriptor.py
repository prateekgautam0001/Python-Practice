grade = input("Enter grade (A-F): ").upper()
match grade:
    case 'A':
        print("Excellent")
    case 'B':
        print("Good")
    case 'C':
        print("Average")
    case 'D':
        print("Poor")
    case 'F':
        print("Fail")
    case _:
        print("Invalid grade")
