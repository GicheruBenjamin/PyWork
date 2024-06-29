

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


# Enumaration(enum.py)

In Python, there are two concepts related to enumeration:

1. enumerate function: This built-in function helps iterate through an iterable(sequences) (like a list, tuple, or string) and get both the index (position) and the element value at that position.The enumerate function takes an iterable and an optional starting index (defaults to 0) as arguments. It returns an enumerate object, which acts as an iterator. In each iteration, it provides a tuple containing the current index and the corresponding element from the iterable.

2. enum module: This module, introduced in Python 3.4, provides a way to create custom enumerations. These are essentially user-defined sets of symbolic names (members) associated with unique values.The enum.Enum class is used to create custom enumerations. It provides a way to define a set of named constants with associated values. This can improve code readability and maintainability by using meaningful names instead of raw integer values.

- Key differences:

enumerate is a function for iterating with index access, while enum is a module for creating custom enumerations with named constants.
enumerate works with any iterable, while enum creates a new class to hold the enumeration members.

## Binary Search (bs.py)
Def :left is 0 and right is arrays end i.e -1 the length. Mid is left + right divide 2.
@Start with the middle element of the array.
@If the middle element is the target value, return its index.
@If the middle element is greater than the target value, search the left half of the array.
@If the middle element is less than the target value, search the right half of the array.
@Repeat steps 1-4 until the target value is found or the search interval is empty.

## Sorting (sortB.py)
sorted(list) for 1st example.
list.sort(function) returns sorted list. Both .sorted(list) and list.sort(function) are equivalent, return sorted lists and built-in functions

## Stacks and queues Simplified(deque.py)
From the collections module u get a deque class in which u can create a stack and a queue from it. It supports ops for it to operate that way. $$FIFO & $$LIFO


