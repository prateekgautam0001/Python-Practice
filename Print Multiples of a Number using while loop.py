num = int(input("Enter base number: "))
limit = int(input("Enter limit: "))
i = 1
while num * i <= limit:
    print(num * i, end=' ')
    i += 1
