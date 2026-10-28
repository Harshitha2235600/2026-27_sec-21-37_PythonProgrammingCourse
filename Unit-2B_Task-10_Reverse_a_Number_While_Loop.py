#Reverse a Number
n = 123
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10
print(f"The reversed number is: {reverse}")