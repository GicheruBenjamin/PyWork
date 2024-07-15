

part : dict = {
    "upper": "head",
    "center": "chest",
    "lower": "legs"
}

# normally 
print(part["center"])
# using get
print(part.get("lower"))
# Normal way of creating a dict
no_of_fruits:dict = {"apples": 5, "oranges": 3, "bananas": 7}
print(no_of_fruits)
#Another way of doing so
no_of_fruits = dict(apples=5, oranges=3, bananas=7)
print(no_of_fruits)#Same output as b4