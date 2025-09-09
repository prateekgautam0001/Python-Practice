command = input("Enter command (start, stop, restart): ").lower()
match command:
    case "start":
        print("System starting...")
    case "stop":
        print("System stopping...")
    case "restart":
        print("System restarting...")
    case _:
        print("Unknown command")
