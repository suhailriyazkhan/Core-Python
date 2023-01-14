s = [1,2,3,4,5,5,5]
d={}

for c in s :
    if c in d.keys():
        d[c] = d[c]+1
    else:
        d[c] =1

print(d)
print(max(d))