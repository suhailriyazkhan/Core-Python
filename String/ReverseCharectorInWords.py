str= "all the power is in you"
temp =str.split()

print(temp)
result=[]
length = len(temp)
i = 0
while i<length:
    Word = temp[i]
    reversedWord = Word[::-1]
    result.append(reversedWord)
    i += 1
print(' '.join(result))
