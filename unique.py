

Using set():
You can convert the list to a set, which automatically removes duplicate elements, and then convert it back to a list.

original_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
unique_list = list(set(original_list))
print(unique_list)
Output: [1, 2, 3, 4, 5, 6]

Using list(set(...)) directly:
You can use the set() conversion directly within the list constructor.

unique_list = list(set([1, 2, 2, 3, 4, 4, 5, 5, 6]))
print(unique_list)
Output: [1, 2, 3, 4, 5, 6]

Using list.append() with a set():
You can iterate through the original list and use a set to keep track of unique elements.

original_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
unique_list = []
unique_set = set()
for num in original_list:
    if num not in unique_set:
        unique_list.append(num)
        unique_set.add(num)
print(unique_list)
Output: [1, 2, 3, 4, 5, 6]

Using a set() comprehension:
You can use a set comprehension to directly create a set of unique elements.

original_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
unique_set = {num for num in original_list}
print(unique_set)
Output: {1, 2, 3, 4, 5, 6}

Using list.count() and filtering:
You can iterate through the list and filter out elements that have a count greater than 1.

original_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
unique_list = [num for num in original_list if original_list.count(num) == 1]
print(unique_list)
Output: [1, 3, 6]

Using collections.Counter:
You can use the Counter class from the collections module to count the occurrences of each element and then filter out duplicates.

from collections import Counter

original_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
counter = Counter(original_list)
unique_list = [item for item in counter if counter[item] == 1]
print(unique_list)
Output: [1, 3, 6]