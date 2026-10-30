# Count Vowels, Consonants, Digits, and Spaces in a String
s = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0

for c in s:
    if c.lower() in "aeiou":
        vowels += 1
    elif c.isalpha():
        consonants += 1
    elif c.isdigit():
        digits += 1
    elif c.isspace():
        spaces += 1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")