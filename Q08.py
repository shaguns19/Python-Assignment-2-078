a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = a + b, a - (a + b) # Demonstrate arithmetic-based swap using updated values
# Recover original pair from the transformed values
b, a = a + b, a - b
print("Swapped values:", a, b)
