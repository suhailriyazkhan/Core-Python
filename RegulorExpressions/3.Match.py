#search only at the begning

import re
str = "Take up one idea. One idea at a time "
res=re.match(r'T\w',str)
# group function invokes only if Something is returned
# group function raise exception when match returns none

print(res.group())