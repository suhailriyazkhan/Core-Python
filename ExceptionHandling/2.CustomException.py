class OverTheLimitException(Exception):
    def __init__(self, message):
        self.message =message

def withdrawl(ammount):
    if (ammount>500):
        raise OverTheLimitException("enter less ammount less than 500")

withdrawl(600)