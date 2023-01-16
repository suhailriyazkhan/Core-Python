# calculating the sum of all elements in a list
from functools import reduce

lst = [5,10,6,9]
res=reduce( lambda x,y:x+y , lst)
print(res)