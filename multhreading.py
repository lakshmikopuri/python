
#creating a thread wihtout using any cls
from threading import *
def display():
    print("this code",current_thread().getName())
#print(" code",current_thread().getName())
t=Thread(target=display)
t.start()
print("his code",current_thread().getName())
#
from threading import*
def display():
    for i in range(10):
        print("chhild threas")
t=Thread(target=display)
t.start()
for i in range(10):
    print("main threda")
#creating a thread using extending
from threading import*
class mythread(Thread):
    def run(self):
        for i in range(10):
            print("childthreda")
t=mythread()
t.start()
for i in range(10):
    print("main threda")
#without extending
from threading import*
class test:
    def display(self):
        for i in range(10):
            print("childthreda")
obj=test()
t=Thread(target=obj.display)
t.start()
for i in range(10):
    print("main threda")
#thread identification number
from threading import*
def display():
    print("child threD",current_thread().ident)

t=Thread(target=display)
t.start()
print("main threda  identification",current_thread().ident)
print("child threda identification",t.ident)
#

from threading import*
import time
def display():
    print("child threD",current_thread().name,"started....")
    time.sleep(3)
    print(current_thread().name,"ende..." )
#print("the nmer of active tjread",active_count())

t1=Thread(target=display,name="child thread 1")
t2=Thread(target=display,name="child thread 2")
t3=Thread(target=display,name="child thread 3")
t1.start()
t2.start()
t3.start()
l=enumerate
#print("the number of active thread:",active_count())
for t in l:
    print("name",t.name)
