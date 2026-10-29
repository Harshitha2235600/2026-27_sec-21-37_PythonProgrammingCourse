#Sum of Digits
n = 123
sum_of_digits = 0
while n > 0:
    digit = n % 10
    sum_of_digits += digit
    n //= 10
print(f"The sum of digits is: {sum_of_digits}")