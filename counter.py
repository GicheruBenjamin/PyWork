from collections import Counter
from time import perf_counter

# Create a list of elements
my_list = [1, 2, 2, 3, 4, 4, 4, 5, 5, 5]

# Create a Counter object
counter = Counter(my_list)

# Print the Counter
print(counter)

print(counter[4])  # Output: 3

print(counter.most_common(2))  # Output: [(4, 3), (5, 3)]from time import perf_counter


# Function to calculate factorial without caching
def factorial_no_cache(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_no_cache(n - 1)

# Function to calculate factorial with caching
def factorial_with_cache(n, cache={}):
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        return 1
    else:
        result = n * factorial_with_cache(n - 1, cache)
        cache[n] = result
        return result

# Measure execution time without caching
start_time = perf_counter()
result_no_cache = factorial_no_cache(400)
end_time = perf_counter()
duration_no_cache = end_time - start_time

# Measure execution time with caching
start_time = perf_counter()
result_with_cache = factorial_with_cache(400)
end_time = perf_counter()
duration_with_cache = end_time - start_time

print(f"Result without caching: {result_no_cache}")
print(f"Execution time without caching: {duration_no_cache:.6f} seconds")

print(f"Result with caching: {result_with_cache}")
print(f"Execution time with caching: {duration_with_cache:.6f} seconds")