text = input("Enter text: ").lower()
vowels = consonants = 0
for ch in text:
    if ch.isalpha():
        if ch in 'aeiou':
            vowels += 1
        else:
            consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
