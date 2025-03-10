# Description: This file contains the solution to the homework 6
# Author: Hermann Kenko Tanfoudie
# Date: 03/04/2025from functools import reduce
from functools import reduce
# 1. Basic Lambda Function: Check if a number is even or odd
even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even_or_odd(5))  # Output: Odd
print(even_or_odd(8))  # Output: Even

# 2. Advanced Lambda Function: Sum of a list
sum_list = lambda numbers: sum(numbers)
print(sum_list([1, 2, 3, 4, 5]))  # Output: 15

# 3. Sorting with Lambda: Sort a list of tuples by second element
pairs = [(1, 5), (3, 2), (4, 8), (2, 3)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(3, 2), (2, 3), (1, 5), (4, 8)]

# 4. Filtering with Lambda: Get even numbers using `filter()`
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8]

# 5. Mapping with Lambda: Square each number using `map()`
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36, 49, 64]

# 6. Reducing with Lambda: Get the product of all numbers using `reduce()`
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 40320 (1*2*3*4*5*6*7*8)

# 7. Enumerate with Lambda: Create index-value pairs
indexed_numbers = list(enumerate(numbers, start=1))
print(indexed_numbers)  # Output: [(1, 1), (2, 2), (3, 3), ..., (8, 8)]

# 8. Zip with or without Lambda: Combine two lists into pairs
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = list(zip(names, ages))
print(combined)  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
