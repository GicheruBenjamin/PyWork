

#Using lambda function
onion : callable = lambda x: lambda y: x + y
print(onion(2)(3))

