
#Strings are of str or sequence type
from typing import  str, Sequence

myname:str = "Izuku"
mypower: Sequence = "Superstrength"

"""Demonstrates various string manipulation techniques."""

# Create strings
string1 = "Hello, world!"
string2 = "Python is awesome"

# Access characters
print("First character:", string1[0])
print("Last character:", string1[-1])

# Slice strings
substring = string1[7:12]
print("Substring:", substring)

# Concatenate strings
concatenated_string = string1 + " " + string2
print("Concatenated:", concatenated_string)

# Repeat strings
repeated_string = string1 * 3
print("Repeated:", repeated_string)

# Check for substring presence
is_present = "world" in string1
print("Is 'world' present?", is_present)

# Find length
length = len(string1)
print("Length:", length)

# String methods
print("Uppercase:", string1.upper())
print("Lowercase:", string1.lower())
print("Capitalized:", string1.capitalize())
print("Index of 'world':", string1.find("world"))
print("Replaced:", string1.replace("world", "everyone"))
print("Split:", string1.split())
print("Joined:", " ".join(["Hello", "there"]))
print("Stripped:", string1.strip())
print("Starts with 'Hello':", string1.startswith("Hello"))
print("Ends with 'world!':", string1.endswith("world!"))