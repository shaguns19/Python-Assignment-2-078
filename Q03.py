a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
if b == 0:
    print("Cannot divide by zero.")
else:
    quotient = a // b
    remainder = a - quotient * b
    print("Remainder:", remainder)
