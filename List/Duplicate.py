s = [1,2,3,4,5,5,5]
d={}

for c in s :
    if c in d.keys():
        d[c] = d[c]+1
    else:
        d[c] =1

print(d)
print(max(d.items()))
#
#
#
# l = [1,5,6,2,8,5,5,6,6,9,1,1]
# x=[]
# print(len(l))
#
# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         if l[i]==l[j] and l[i] not in x:
#             x.append(l[i])
# print(l)
# print(x)
# print(max(x))
#
#
#
#
# """l = [1,5,6,2,8,5,5,6,6,9,1,1]
# n = len(l)
#
# def findDuplicate(l,n):
#     print(l,n)
#     if n<=1:
#         return -1
#     x =[]
#     c=0
#     while c<n-1:
#         j = c+1
#         if l[c] == l[j] and l[c] not in x:
#             x.append(l[c])
#         c+= 1
#     return x
#
# print(findDuplicate(l,n))"""

dup=[]
for ele in s:
    if ele not in dup:
        dup.append(ele)
print(max(dup))





























