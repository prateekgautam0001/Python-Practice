filename = input("Enter filename: ")
ext = filename.split('.')[-1]
match ext:
    case "py":
        print("Python file")
    case "txt":
        print("Text file")
    case "jpg" | "png":
        print("Image file")
    case "pdf":
        print("PDF document")
    case _:
        print("Unknown file type")
