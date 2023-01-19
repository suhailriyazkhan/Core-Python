"""  we can use Quantifiers to match multiple charectors
+ , *, ? {m}, {m,n}, \d+  """
#return a list all tha string match

import re
str = "oh my name is Suhail khan omg"
result = re.findall(r'o\w{1}',str)
print(result)
