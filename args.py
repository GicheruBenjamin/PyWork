
# Having the option for a lot of arguments in your functions

#Normal function
def work(time: tuple[str,float], weather: str) -> str:
    return f"I worked on {time[0]} at {time[1]} and it was {weather}"

my_day = work(("Monday", 8), "sunny")
print(my_day)

# Same function with args in the function creation
def hiswork(*args):
    return f"I worked on {args[0]} at {args[1]} and it was {args[2]}"

dani_day = hiswork("Tuesday", 8, "windy")
print(dani_day)