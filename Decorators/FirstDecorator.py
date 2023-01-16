def decor(fun):
     def inner():
         result = fun()
         return result*2
     return inner

# def myfun():
#     return 10
# usingdecor = decor(myfun)
# print(usingdecor())

@decor
def myfun():
    return 10
print(myfun())
