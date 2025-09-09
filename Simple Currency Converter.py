amount = float(input("Amount in USD: "))
currency = input("Convert to (EUR, INR, GBP): ").upper()
match currency:
    case "EUR":
        print("Amount in EUR:", amount * 0.85)
    case "INR":
        print("Amount in INR:", amount * 83.0)
    case "GBP":
        print("Amount in GBP:", amount * 0.75)
    case _:
        print("Unsupported currency")
