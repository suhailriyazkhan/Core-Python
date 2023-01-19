from threading import *
from time import *

class Producer:
    def __init__(self):
        self.product = []
        self.c = Condition()

    def produce(self):
        self.c.acquire()

        for i in range(1, 5):
            self.product.append("product" + str(i))
            sleep(1)
            print("item added")
        self.c.notify()
        self.c.release()

class Consumer:
    def __init__(self, prod):
        self.prod = prod
    def consume(self):
        self.prod.c.acquire()
        self.prod.c.wait(timeout=0)
        self.prod.c.release()
        print("Order Shipped" , self.prod.product)


p =Producer()
c = Consumer(p)

t1 = Thread(target=p.produce)
t2 = Thread(target = c.consume)

t1.start()
t2.start()