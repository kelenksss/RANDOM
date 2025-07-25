import random

# Generate 5 random numbers between 0 and 10
num_1 = random.randint(0, 10)
num_2 = random.randint(0, 10)
num_3 = random.randint(0, 10)
num_4 = random.randint(0, 10)
num_5 = random.randint(0, 10)

# Print all generated numbers with labels (without f-strings)
print("num 1:", num_1)
print("num 2:", num_2)
print("num 3:", num_3)
print("num 4:", num_4)
print("num 5:", num_5)

# Print the maximum number among them
print("max:", max(num_1, num_2, num_3, num_4, num_5))