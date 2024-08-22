from threading import *
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)
ObjHello=Hello()
ObjHi=Hi()
# ObjHello.run()
# ObjHi.run()
ObjHello.start()
sleep(0.2)
ObjHi.start()
ObjHello.join()
ObjHi.join()
print("Bye")
