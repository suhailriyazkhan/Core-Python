str= "all the power is in you"
temp =str.split()

print(temp)
result=[]
i = len(temp)-1
while i>=0:
    result.append(temp[i])
    i -= 1
print(' '.join(result))


