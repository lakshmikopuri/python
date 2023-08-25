def wish(name):
    print("gud evening",name)
wish("lucky")
def square(x):
    print("the square of {} is : {}  ".format(x,x*x))
square(10)
def add(a,b):
    return a+b
result=add(100,200)
print(result)
def evenodd(n):
    if(n%2==0):
        print("the given nnnum {} is even".format(n))
    else:
         print("the given nnnum {} is odd".format(n))
n=int(input())
evenodd(n)
#positional argu
def pos(a,b):
    print(a-b)
pos(100,200)
#keywrd
def keywrd(name,msg):
    print(name,msg)
keywrd(name="lucky",msg="god mrng")
#deafult
def defalult(name="lucky"):
    print(name)
defalult()
#var lenth argu
def calc(*n):
    res=0 
    for x in n:
        res+=x 
    print(res)
calc(10,20)
calc(10)
calc(10,30,70)
#variable lenth keywrd
def displa(**kwargs):
    print("record info")
    for k,v in kwargs.items():
        print(k,"...........",v)
displa(name="lucky",marks="100",age="40")
