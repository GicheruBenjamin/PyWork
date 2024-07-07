


original_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
unique_list = list(set(original_list))
print(unique_list)


unique_list = list(set([1, 2, 2, 3, 4, 4, 5, 5, 6]))
print(unique_list)

original_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
unique_list = []
unique_set = set()
for num in original_list:
    if num not in unique_set:
        unique_list.append(num)
        unique_set.add(num)
print(unique_list)


original_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
unique_set = {num for num in original_list}
print(unique_set)
Output: {1, 2, 3, 4, 5, 6}


original_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
unique_list = [num for num in original_list if original_list.count(num) == 1]
print(unique_list)



from collections import Counter

original_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
counter = Counter(original_list)
unique_list = [item for item in counter if counter[item] == 1]
print(unique_list)
