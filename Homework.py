import random
# List of square numbers
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Pick a random number from the list
number = random.choice(squares)

# Calculate the square root using the exponent operator
square_root = number ** 0.5

# Added 'f' before the string so {number} and {square_root} work properly
print(f"The square root of {number} is {square_root}")