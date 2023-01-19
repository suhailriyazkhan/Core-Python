#return a list all tha string match

import re
str = " oh my name is suhail khan omg "
result=re.findall(r'o\w',str)
print(result)