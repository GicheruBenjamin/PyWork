from typing import List 

my_snacks:List[str] = ["soda", "cookies", "biscuits", "cereal"]

for i , snack in enumerate(my_snacks):
    print(i, snack)
    
from enum import Enum

class teachers(Enum):
    HOD = "head of department"
    LEC= "lecturer"
    ASSIST = "assistant"
    PROF = "professor"
    ASSPROf = "assistant professor"
    INST = "instructor"
    TR = "teacher"
    OTH = "other"
    
print(teachers.LEC.value) # Output "lecturer"