role = input("Enter your role (admin, user, guest): ").lower()
match role:
    case "admin":
        print("Full access")
    case "user":
        print("Limited access")
    case "guest":
        print("Read-only access")
    case _:
        print("Unknown role")
