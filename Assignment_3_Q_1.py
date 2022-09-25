
# Q.1) Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total
print(sum((8, 2, 3, 0, 7)))