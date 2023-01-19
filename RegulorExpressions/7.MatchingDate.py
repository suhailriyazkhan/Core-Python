#search only at the begning

import re
str = "Take 1 up 1-3-2019 one 23 idea. One idea 45 at a time 12-11-2020"

res=re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)

print(res)