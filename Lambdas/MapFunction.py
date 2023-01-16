lst = [1,22,33,55,66]
result= map(lambda x: x*2, lst)
print(list(result))

str = "1 2 3 5 6"

"""result =map(int, str.split())
print(list(result))"""
#or
result= list(map(int, input().split()))
print(result)
