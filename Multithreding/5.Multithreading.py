from threading import *
from time import sleep


class Mythread:
    def displayNumbers(self):
        i = 0
        print(current_thread().getName())
        sleep(1)
        while (i <= 10):
            print(i)
            i += 1

obj = Mythread()
t = Thread(target=obj.displayNumbers())
t.start()
t = Thread(target=obj.displayNumbers())
t.start()
t = Thread(target=obj.displayNumbers())
t.start()
