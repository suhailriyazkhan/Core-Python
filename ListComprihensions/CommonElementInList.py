"""a = [1,2,3,3,5]
b = [1,2,6,3,9]'''
z=[]
for i in a:
    if i in b and i not in z:
        z.append(i)
print(z)"""

a = [1,2,3,3,5]
b = [1,2,6,3,9]

lst = [i for i in a if i in b ]
print(set(lst))

