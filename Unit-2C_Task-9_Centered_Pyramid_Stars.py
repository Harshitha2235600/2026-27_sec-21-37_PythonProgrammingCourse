#Centered Pyramid of Stars
n = int(input("Enter the size of the pyramid: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))