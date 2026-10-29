
n = 5
for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(i + 1):
        if j == 0 or j == i:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()