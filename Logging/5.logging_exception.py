import logging
logging.basicConfig(filename="mylog", level=logging.DEBUG)
try:
    a=10
    b=0
    c=a/b

#executes when exception occurs
except ZeroDivisionError:
    print("division by zero not allowed")
    logging.error("Dvivision by zero")
#executes when no exception occurs after try block
else:
    print("you have entered a non zero number")

#execute evertime
finally:
    print("file closed")



