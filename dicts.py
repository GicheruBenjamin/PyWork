



# Creating a dictionary with string keys and various value types
my_dict = {
    'name': 'John', 
    'age': 30,  
    'city': 'New York', 
    'is_student': True,  
    'favorite_numbers': [1, 2, 3],  
    'skills': {'programming': 'Python', 'language': 'English'}, 
}

# Accessing dictionary items using keys
print(my_dict['name'])  
print(my_dict['age']) 
print(my_dict['city'])  
print(my_dict['is_student'])  
print(my_dict['favorite_numbers'])  
print(my_dict['skills'])  

# Adding a new key-value pair to the dictionary
my_dict['country'] = 'USA'
print(my_dict)

# Updating an existing key-value pair in the dictionary
my_dict['age'] = 31
print(my_dict)

# Removing a key-value pair from the dictionary
del my_dict['is_student']
print(my_dict)

# Checking if a key exists in the dictionary
if 'name' in my_dict:
    print("The 'name' key exists in the dictionary.")
    
# Iterating over the dictionary keys, values, and items
for key in my_dict.keys():
    print(key)
    
    
for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)


# Using dictionary methods
print(my_dict.get('name'))  
print(my_dict.get('country', 'Unknown')) 
print(my_dict.setdefault('state', 'New York'))  
print(my_dict)

# Copying a dictionary
my_dict_copy = my_dict.copy()
print(my_dict_copy)

# Clearing a dictionary
my_dict_copy.clear()
print(my_dict_copy)  
# Normal way of creating a dict
no_of_fruits:dict = {"apples": 5, "oranges": 3, "bananas": 7}
print(no_of_fruits)
#Another way of doing so
no_of_fruits = dict(apples=5, oranges=3, bananas=7)
print(no_of_fruits)#Same output as b4