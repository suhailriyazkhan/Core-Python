#split the string in to a list

import re
str = "Take up one idea.One idea at a time"
res = re.split(r'\d+',str)

print(res)