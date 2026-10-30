# Count the frequency of each character in a string
s = input("Enter a string: ")
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
for c, f in freq.items():
    print(f"Character '{c}': {f} times")