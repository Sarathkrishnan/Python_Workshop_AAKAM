a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Swap without using a temporary variable
a, b = b, a

# Display the result
print(f"After swapping: a = {a}, b = {b}")