str = "abcccdeffgh"
temp =[]
for i in str:
    if i not in temp:
        temp.append(i)
print(temp)
print(''.join(temp))