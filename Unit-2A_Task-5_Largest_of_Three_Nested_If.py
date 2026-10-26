# Largest of Three Numbers using Nested If
a = 10
b = 20
c = 30

if a > b:
    if a > c:
        print("Largest is:", a)
    else:
        print("Largest is:", c)
else:
    if b > c:
        print("Largest is:", b)
    else:
        print("Largest is:", c)