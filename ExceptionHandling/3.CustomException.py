class TooYoungException(Exception):
    def __init__(self, message):
        self.message = message

class TooOldException(Exception):
    def __init__(self, message):
        self.message = message

age =int(input("enter the age"))

if age <18:
    raise TooYoungException("age can not be less than 18")

if age >90:
    raise TooYoungException("age can not be greater than 90")

else:
    print("congratulation access granted")



