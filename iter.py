

my_set = {1, 2, 3, "apple"}
for element in my_set:
  print(element)
  
my_tuple = (1, "apple", 3.14)
for i in range(len(my_tuple)):
  print(my_tuple[i])
  
for n in my_tuple:
  print(n)
  
my_dict = {"name": "Mercy",
"age": 30, 
"city": "New York"
}
for key in my_dict:
  print(key, my_dict[key])
  
for key, value in my_dict.items():
  print(key, value)

for value in my_dict.values():
  print(value)
  
  
my_loc = '12E', '5N', '8W', '2S'; print(type(my_loc)) 


from typing import Iterator, Iterable

def my_generator(data: Iterable[int]) -> Iterator[int]:
    for num in data:
        yield num * 2

def process_data(data: Iterator[str]) -> None:
    for item in data:
        print(item.upper())

# Example usage:
numbers = [1, 2, 3]  # Iterable of integers
doubled_numbers = my_generator(numbers)  # Iterator of integers

process_data(iter(["hello", "world"]))  # Using an iterator directly