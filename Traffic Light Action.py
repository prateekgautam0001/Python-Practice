light = input("Traffic light color: ").lower()
match light:
    case "red":
        print("Stop")
    case "yellow":
        print("Slow down")
    case "green":
        print("Go")
    case _:
        print("Invalid color")
