s = input("Enter a string: ")
start = int(input("Start index to remove: "))
end = int(input("End index to remove: "))
new_s = s[:start] + s[end:]
print("Modified string:", new_s)
