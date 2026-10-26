# Smallest of Three Numbers using Nested If
a = 10
b = 20
c = 30

if a < b:
    if a < c:
        print("Smallest is:", a)
    else:
        print("Smallest is:", c)
else:
    if b < c:
        print("Smallest is:", b)
    else:
        print("Smallest is:", c)