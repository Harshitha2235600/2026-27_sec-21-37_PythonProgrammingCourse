a=float(input("Enter the first angle:"))
b=float(input("Enter the second angle:"))
c=float(input("Enter the third angle:"))
sum=a+b+c
if a>0 and b>0 and c>0 and sum==180:
    print("The triangle is valid")
else:
    print("The triangle is not valid")


