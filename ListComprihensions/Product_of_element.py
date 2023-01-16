"""a = [1,2,3,3,5]
b = [1,2,3,3,5]
z=[]
print(len(a))
for i in range(len(a)):
    z.append(a[i]*b[i])
print(z)"""

a = [1,2,3,3,5]
b = [1,2,3,3,5]

lst = [ a[x]*b[x] for x in range(len(a))]
print(lst)


