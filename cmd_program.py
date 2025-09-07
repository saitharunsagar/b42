import sys

# Check if two arguments are passed
if len(sys.argv) != 3:
    print("Usage: python add_numbers.py <num1> <num2>")
    sys.exit(1)

# Get the arguments
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

# Add and print the result
result = num1 + num2
print(f"The sum is: {result}")
