from typing import List
from statistics import mean , mode , median
stud_marks: List[int] = [50, 62, 71, 84, 29, 45]
mean_marks: int = mean(stud_marks)
median_marks: int = median(stud_marks)
mode_marks: int = mode(stud_marks)
print(mean_marks)
print(median_marks)
print(mode_marks)