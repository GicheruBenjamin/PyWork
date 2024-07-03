

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
  
  
my_loc = '12E', '5N', '8W', '2S'; print(type(my_loc)) #output <class 'tuple'>