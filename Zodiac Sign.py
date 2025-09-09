month = input("Enter birth month: ").lower()
day = int(input("Enter birth day: "))
match month:
    case "march" if day >= 21 or (month == "april" and day <= 19):
        print("Aries")
    case "april" if day >= 20 or (month == "may" and day <= 20):
        print("Taurus")
    case "may" if day >= 21 or (month == "june" and day <= 20):
        print("Gemini")
    case "june" if day >= 21 or (month == "july" and day <= 22):
        print("Cancer")
    case "july" if day >= 23 or (month == "august" and day <= 22):
        print("Leo")
    case _:
        print("Other Zodiac or Invalid Date")
