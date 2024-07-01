# List to Tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print("List to Tuple:", my_tuple)

# Tuple to List
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print("Tuple to List:", my_list)

# List/Tuple to Set
my_iterable = [1, 2, 2, 3, 4, 4]
my_set = set(my_iterable)
print("List/Tuple to Set:", my_set)

# Set to List/Tuple
my_set = {1, 2, 3, 4, 5}
my_list = list(my_set)
my_tuple = tuple(my_set)
print("Set to List:", my_list)
print("Set to Tuple:", my_tuple)

# Dictionary to List of Tuples
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_list_tuples = list(my_dict.items())
print("Dictionary to List of Tuples:", my_list_tuples)

# List of Tuples to Dictionary
my_list_tuples = [('a', 1), ('b', 2), ('c', 3)]
my_dict = dict(my_list_tuples)
print("List of Tuples to Dictionary:", my_dict)

# String to List/Tuple
my_string = "abcde"
my_list = list(my_string)
my_tuple = tuple(my_string)
print("String to List:", my_list)
print("String to Tuple:", my_tuple)