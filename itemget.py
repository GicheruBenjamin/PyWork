from typing import List, Tuple
from operator import itemgetter

els : List[int] = [1, 2, 3, 4, 5]
# A tuple of 1st and last elements of the list
fandl:Tuple[int,int] = itemgetter(0, -1)(els)
print(fandl)