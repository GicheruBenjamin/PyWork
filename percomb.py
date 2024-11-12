

from itertools import combinations, permutations

# Example set of elements
elements = [1, 2, 3]
print (elements)

# Generate and print combinations of size 2
print("Combinations of size 2:")
for combo in combinations(elements, 2):
    print(combo)

# Generate and print all permutations of the elements
print("\nAll permutations:")
for perm in permutations(elements):
    print(perm)

# Generate and print permutations of size 2
print("\nPermutations of size 2:")
for perm in permutations(elements, 2):
    print(perm)