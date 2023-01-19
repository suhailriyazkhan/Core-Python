import re

str =" my name is suhail khan"
result = re.search(r's\w\w',str)
print(result.group())