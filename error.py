
from time import sleep
## 1st way to handle errors
a: str = "hello"
try:
    print(float(a))
except:
    print(f"{a} can't be converted to a float")
    
## 2nd way to handle errors
c: str = "hello"
try:
    print(float(a))
except ValueError:
    print(f"{a} can't be converted to a float")
finally:
    sleep(10)
    print("done")

axis: tuple = (2, 3)
try:
    print(axis[3])
except IndexError:
    print("Index out of range")

