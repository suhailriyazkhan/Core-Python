from threading import *

class BookMybuss:
    def buy(self):
        print("confirmed seat")

obj =BookMybuss()

t1 = Thread(target=obj.buy())
t2 = Thread(target=obj.buy())
t3 = Thread(target=obj.buy())

t1.start()
t2.start()
t3.start()