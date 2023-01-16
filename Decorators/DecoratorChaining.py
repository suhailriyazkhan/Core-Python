def suare(fun):
    def inner():
        result = fun()
        return result ** 2

    return inner

def half(fun):
    def inner():
        result = fun()
        return result /2

    return inner


@suare
@half
def myfun():
    return 10

print(myfun())