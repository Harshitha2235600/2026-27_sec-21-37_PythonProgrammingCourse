#Largest in Series of N Numbers using For Loop
n = int(input("Enter the number of elements: "))
largest = float('-inf')  # Initialize to negative infinity
for i in range(n):
    element = int(input("Enter element {}: ".format(i+1)))
    if element > largest:
        largest = element
print("The largest element is:", largest)