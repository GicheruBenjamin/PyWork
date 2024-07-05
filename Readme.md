

# Itarations in data sructures in Py (iter.py)

- Sets

Sets are unordered collections of unique elements. Since they are unordered, you cannot iterate through them by index. However, Python provides ways to loop through their elements.For loop will print each element in the set on a new line. The order may vary in each run as sets are unordered.

- Tuples:

Tuples are ordered sequences of elements, similar to lists. They are immutable, meaning elements cannot be changed after creation.
1. for loop with index
A loop iterates through the indices of a tuple and uses them to access elements using bracket notation.
2. for loop with unpacking
A loop unpacks the elements of the tuple into variablesin each iteration.

  **note** - Did u know unless you having an empty tuple u don't need brackets Now U know. 

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

## Counter (counter.py)
The Counter class from the collections module in Python is a powerful tool for counting occurrences of elements in a collection, such as a list, tuple, or string. Here's a quick reference document on the Counter class, including its commonly used methods and operations:
Counter Class in Python:
Importing: Import the Counter class from the collections module using from collections import Counter.
Creation: Create a Counter object by passing an iterable (list, tuple, string, etc.) to the Counter constructor. For example, counter = Counter([1, 2, 2, 3]).
Output Format: The Counter object displays elements as keys and their counts as values. Example: Counter({2: 2, 1: 1, 3: 1}).
Accessing Counts: Access the count of a specific element using square brackets. Example: print(counter[2]).
Most Common Elements: Find the most common elements using the most_common() method. Example: print(counter.most_common(3)).
Element Presence: Check if an element is present in the Counter using the contains() method. Example: if 2 in counter: ....
Updating Counts: Update the count of an element using the update() method. Example: counter.update([2, 3, 3]).
Combining Counters: Combine two Counter objects using arithmetic operations like +, -, or &. Example: new_counter = counter1 + counter2.
Subtracting Counters: Subtract one Counter from another using the - operator. Example: difference_counter = counter1 - counter2.
Element Removal: Remove an element from the Counter using the subtract() method. Example: counter.subtract([2]).
Clearing Counter: Clear all counts using the clear() method. Example: counter.clear().
Total Count: Get the total count of all elements using the total() method. Example: total_count = counter.total().
Elements with Zero Count: Get elements with zero count using the elements() method. Example: zero_count_elements = counter.elements() & counter2.elements().
Iteration: Iterate over elements and their counts using the items() method. Example: for item, count in counter.items(): ....
Dictionary Conversion: Convert the Counter to a dictionary using the dict() method. Example: counter_dict = counter.dict().
List of Elements: Get a list of unique elements using the keys() or elements() method. Example: unique_elements = counter.keys().
The Counter class is particularly useful for tasks involving frequency analysis, counting occurrences, and finding the most common elements in a collection. It provides an efficient and convenient way to work with data where element counts are important.

## Conversion of types(conv.py)
List to Tuple: When you want to create an immutable sequence of elements.
Tuple to List: When you need to modify the elements or perform operations that require a mutable sequence.
List/Tuple to Set: To remove duplicate elements and create a unique collection.
Set to List/Tuple: To convert a unique collection back to a sequence.
Dictionary to List of Tuples: To iterate over key-value pairs or to create a sorted list of keys/values.
List of Tuples to Dictionary: To create a dictionary from a list of key-value pairs.
String to List/Tuple: To treat a string as a sequence of characters for processing or manipulation.

## Reasons for type conversion{doc} 
Data structure conversions, also known as type conversions, offer several advantages and are useful in various scenarios. Here are some reasons why you might want to perform certain types of conversions, along with their advantages in terms of methods and properties:
- List to Tuple:
Advantage: Immutability. Converting a list to a tuple makes the sequence immutable, preventing accidental modifications.
Methods/Properties: Tuples support methods like count(), index(), and index() for element counting and searching.
- Tuple to List:
Advantage: Mutability. Converting a tuple to a list allows you to modify the elements, add or remove items, and perform operations that require a mutable sequence.
Methods/Properties: Lists provide methods like append(), insert(), pop(), sort(), and more for efficient manipulation.
- List/Tuple to Set:
Advantage: Removing duplicates. Converting a list or tuple to a set eliminates duplicate elements, resulting in a unique collection.
Methods/Properties: Sets offer methods like union(), intersection(), difference(), and symmetric_difference() for set operations.
- Set to List/Tuple:
Advantage: Ordered sequence. Converting a set to a list or tuple allows you to create an ordered sequence of unique elements.
Methods/Properties: Lists and tuples provide indexing, slicing, and iteration capabilities.
- Dictionary to List of Tuples:
Advantage: Iteration and sorting. Converting a dictionary to a list of tuples enables you to iterate over key-value pairs or sort the keys/values separately.
Methods/Properties: The resulting list of tuples retains the properties of tuples, allowing access to individual key-value pairs.
- List of Tuples to Dictionary:
Advantage: Efficient key-based access. Converting a list of tuples to a dictionary allows you to access values using keys efficiently.
Methods/Properties: Dictionaries provide methods like get(), keys(), values(), items(), and more for dictionary manipulation.
- String to List/Tuple:
Advantage: Character-level processing. Converting a string to a list or tuple allows you to treat the string as a sequence of characters, enabling character-level manipulation and analysis.
- Methods/Properties: Lists and tuples provide indexing, slicing, and iteration capabilities for character-level operations.
In summary, data structure conversions offer advantages such as immutability, mutability, duplicate removal, ordered sequences, 
efficient key-based access, and character-level processing. The choice of conversion depends on the specific requirements of your program, including the need for immutability, uniqueness, efficient access, and the desired methods or properties provided by the target data structure.

## Styling your output(styit.py)
You can style your output of your iterable by unpacking it 1st , then add a seperator(sep = '') and then and something at the end (end = '' I have used a line break)

## Working with files(filer.py)
There are several ways to work with files. 1st the usual way by .open & .close. This allows memeory leaks that why the 2nd way is much recommended. Using a with block for ensuring that the file is closed well.

##  Class Composition(cl.py)
Composition involves defining a class that includes instances of other classes as its attributes. This allows you to create complex objects by combining simpler objects. The composite class can provide methods and properties that interact with the contained instances, offering a higher level of abstraction and functionality.In the code, I have three classes: Address, Person, and Employee. The Employee class demonstrates composition by containing instances of the Person and Address classes as its attributes. The Employee class provides a higher-level abstraction by encapsulating the Person and Address instances and offering a method to retrieve employee information

## Caching(cache.py)
In the commented example it takes long time to finish the operation but due to use of lru cache from func_tools it takes less time to complete the operation in the operation.