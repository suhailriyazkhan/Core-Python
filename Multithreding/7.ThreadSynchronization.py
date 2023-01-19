"""we can sync the threads by using lock and semaphore
 so that threads do not affect each other"""


from threading import *

#1. Using Lock
"""class BookMybuss:
    def __init__(self, availableSeats):
        self.availableSeats= availableSeats
        self.l = Lock()

    def buy(self, seatRequested):
        self.l.acquire()
        print("Total seats available: ",self.availableSeats)
        if (self.availableSeats>=seatRequested):
            print(seatRequested,"seat confirmed")
            self.availableSeats -= seatRequested
        else:
            print("sorry no seats available")
        self.l.release()

obj =BookMybuss(10)

t1 = Thread(target=obj.buy(6,))
t2 = Thread(target=obj.buy(6,))
t3 = Thread(target=obj.buy(1,))

t1.start()
t2.start()
t3.start() """

#2.Using semaphore
class BookMybuss:
    def __init__(self, availableSeats):
        self.availableSeats= availableSeats
        self.l = Semaphore()

    def buy(self, seatRequested):
        self.l.acquire()
        print("Total seats available: ",self.availableSeats)
        if (self.availableSeats>=seatRequested):
            print(seatRequested,"seat confirmed")
            self.availableSeats -= seatRequested
        else:
            print("sorry no seats available")
        self.l.release()

obj =BookMybuss(10)

t1 = Thread(target=obj.buy(6,))
t2 = Thread(target=obj.buy(6,))
t3 = Thread(target=obj.buy(1,))

t1.start()
t2.start()
t3.start()