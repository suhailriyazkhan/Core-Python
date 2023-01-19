from threading import *

class Mythread:
    def displayNumbers(self):
        i = 0
        print(current_thread().getName())
        while (i <= 10):
            print(i)
            i += 1

obj = Mythread()
t = Thread(target=obj.displayNumbers())
t.start()