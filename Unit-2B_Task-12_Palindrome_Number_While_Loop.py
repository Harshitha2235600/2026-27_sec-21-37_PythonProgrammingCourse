#Palindrome Number
n = 121
temp = n
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
if reverse == n:
    print(f"{n} is a palindrome number.")
else:
    print(f"{n} is not a palindrome number.")