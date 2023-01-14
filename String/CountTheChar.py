s = "aaaaabbbccccczcfvsddddd"
d={}

for c in s :
    if c in d.keys():
        d[c] = d[c]+1
    else:
        d[c] =1

print(d)
