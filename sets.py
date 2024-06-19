my_set = {1, 2, 3, 4, 5}
print(my_set)  

my_set.add(6)
print(my_set) 

my_set.remove(3)
print(my_set)  

print(my_set.discard(7))  

print(my_set.pop()) 

print(my_set.clear())  

print(my_set.copy())  

print(my_set.difference({1, 2})) 

print(my_set.intersection({1, 2}))

print(my_set.union({1, 2})) 

print(my_set.issubset({1, 2, 3, 4, 5, 6})) 

print(my_set.issuperset({1, 2}))  

print(my_set.isdisjoint({6, 7}))  