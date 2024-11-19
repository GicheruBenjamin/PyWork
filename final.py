
from typing import Final

#Define a varible as a final 
PI: Final[float] = 3.141592653589793
print(PI)

#Using final in a function return value
def get_pi() -> Final[float]:
    return 3.141592653589793

#decorator for printing the values
def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

#Using the decorator to calculate te area  where the area is final
@my_decorator
def calculate_area(radius: Final[float]) -> Final[float]:
    return 3.141592653589793 * radius ** 2