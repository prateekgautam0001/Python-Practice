lst = input("Enter list elements separated by space: ").split()
seen = []
duplicates = []
for item in lst:
    if item in seen and item not in duplicates:
        duplicates.append(item)
    else:
        seen.append(item)
print("Duplicates:", duplicates)
