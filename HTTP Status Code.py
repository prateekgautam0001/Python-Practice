code = int(input("Enter HTTP status code: "))
match code:
    case 200:
        print("OK")
    case 301:
        print("Moved Permanently")
    case 400:
        print("Bad Request")
    case 401:
        print("Unauthorized")
    case 403:
        print("Forbidden")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown code")
