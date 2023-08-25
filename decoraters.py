s=lambda a,b:a if a>b else b
print("thwe big of {} and {} is {}:".format(10,20,s(10,20)))
#filter
def iseven(x):
    if(x%2==0):
        return True
    else:
        return False
l=[10,20,30,40]
l1=list(filter(iseven,l))
print(l1)
#lambda
l = [3, 5, 2, 1, 4, 6]
l1=list(filter(lambda x:x%2==0,l))
print(l1)
#map
l = [3, 5, 2, 1, 4, 6]
l1=list(map(lambda x:2*x,l))
print(l1)

l = [3, 5, 2, 1, 4, 6]
l1=[8,3,4,5,7]
l3=list(map(lambda x,y:y*x,l,l1))
print(l3)
#reduce
from functools import reduce
l=[1,2,3,4]
rees=reduce(lambda x,y:x+y,l)
print(rees)
#decoraters
def dec(func):
    def inner(name):
        print("dec fun exicute")
        func(name)
    return inner
@dec
def wish(name):
    print("hello",name)
wish("lucky")
#2dec
def dec(func):
    def inner(name):
        print("dec fun exicute")
        func(name)
    return inner
def dec2(func):
    def inner(name):
        print("sec dec")
        func(name)
    return inner
@dec2
@dec
def wish(name):
    print("hello",name)
wish("lucky")
    
#
def dec(func):
    def inner():
       x=func()
       return x*x
    return inner
def dec1(func):
    def inner():
       x=func()
       return 2*x
    return inner
@dec1
@dec
def num():
    return 10
print(num())