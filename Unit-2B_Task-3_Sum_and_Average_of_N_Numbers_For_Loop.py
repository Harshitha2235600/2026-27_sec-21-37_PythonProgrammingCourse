#Sum and Average of N Numbers using For Loop
n = int(input("Enter the number of elements: "))
sum = 0
for i in range(n):
    element = int(input("Enter element {}: ".format(i+1)))
    sum += element
average = sum / n if n > 0 else 0
print("Sum of the elements is:", sum)
print("Average of the elements is:", average)