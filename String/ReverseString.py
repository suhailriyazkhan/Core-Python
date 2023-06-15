#1. using slicing

inp="suhail"
print(len(inp))
print(inp[::-1])

#2. reverse using logic
s= input("enter a string: ")
i = len(s)-1
result = ""

while (i>=0):
    result=result+s[i]
    i -= 1
print(result)

#3. using split and join function
x = '-'.join(['a','b','c'])
print(x)
z=input("Enter string")
print(''.join(reversed(z)))

#reversed return an iterator over the given sequence



# str = "my name is suhail khan"
#
# #print([str[::-1]])
#
# splited = str.split()
# print(splited)
# l=[]
# l.extend(reversed(splited))
# print(l)
# print(" ".join(l))



