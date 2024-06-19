

my_set = {1, 2, 3, "apple"}
for element in my_set:
  print(element)
  
my_tuple = (1, "apple", 3.14)
for i in range(len(my_tuple)):
  print(my_tuple[i])
  
my_tuple = (1, "apple", 3.14)
for num, fruit, pi in my_tuple:
  print(num, fruit, pi)