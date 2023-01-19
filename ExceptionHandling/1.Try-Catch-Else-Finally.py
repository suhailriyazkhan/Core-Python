try:
    a=10
    b=10
    c=a/b

#executes when exception occurs
except ZeroDivisionError:
    print("division by zero not allowed")

#executes when no exception occurs after try block
else:
    print("you have entered a non zero number")

#execute evertime
finally:
    print("file closed")



