
i = 0
while i < 3:
    i+=2
    print(i)
    
for i in range(0,12):
    print(i)
    
for k in range(0,12,2):
    print(f"{k} is an even number")
    
#Loop generator
my_gen = (x**2 for x in range(5))
print(my_gen)