n = int(input("Enter an integer: "))
rev = 0; n = abs(n)
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Reversed:", rev)
