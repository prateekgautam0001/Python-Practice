start = int(input("Enter start: "))
end = int(input("Enter end: "))
for num in range(start, end + 1):
    power = len(str(num))
    total = sum(int(d) ** power for d in str(num))
    if total == num:
        print(num, end=' ')
