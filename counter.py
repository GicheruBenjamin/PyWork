from collections import Counter

# Create a list of elements
my_list = [1, 2, 2, 3, 4, 4, 4, 5, 5, 5]

# Create a Counter object
counter = Counter(my_list)

# Print the Counter
print(counter)

print(counter[4])  # Output: 3

print(counter.most_common(2))  # Output: [(4, 3), (5, 3)]