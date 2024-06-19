

# Itarations in data sructures in Py (iter.py)

- Sets

Sets are unordered collections of unique elements. Since they are unordered, you cannot iterate through them by index. However, Python provides ways to loop through their elements.For loop will print each element in the set on a new line. The order may vary in each run as sets are unordered.

- Tuples:

Tuples are ordered sequences of elements, similar to lists. They are immutable, meaning elements cannot be changed after creation.
1. for loop with index
A loop iterates through the indices of a tuple and uses them to access elements using bracket notation.
2. for loop with unpacking
A loop unpacks the elements of the tuple into variablesin each iteration.

- Dictionaries:

Dictionaries are collections of key-value pairs. Keys must be unique and immutable. There are multiple ways to iterate through dictionaries depending on what you want to access.
1. for loop with keys:
A loop iterates through the keys of the dictionary. To access the corresponding value, you can use the key as an index within square brackets on the dictionary (my_dict[key]).
2. for loop with items:
A loop uses the items() method of the dictionary. It returns a view object containing key-value pairs as tuples. The loop unpacks each tuple into key and value variables.
3. for loop with values:
A loop uses the values() method to get a view object containing only the values of the dictionary. The loop iterates through each value directly.
