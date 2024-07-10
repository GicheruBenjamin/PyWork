

part : dict = {
    "upper": "head",
    "center": "chest",
    "lower": "legs"
}

# normally 
print(part["center"])
# using get
print(part.get("lower"))