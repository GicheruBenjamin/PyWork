

from functools import lru_cache

'''def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

for i in range(40):
    print(f"fib({i}) = {fib(i)}")'''
    

@lru_cache(maxsize=3) 
def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

for i in range(40):
    print(f"fib({i}) = {fib(i)}")       
    
for i in range(40):
    print(f"fib({i}) = {fib(i)}")