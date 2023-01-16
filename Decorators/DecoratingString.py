def decor(fun):
    def inner(n):
        result = fun(n)
        return result + "how are you "
    return inner

@decor
def myfun(name):
    return "hello "+ name

print(myfun("suhail "))