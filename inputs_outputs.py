#how to read i/pform keyboard
'''x=int(input())
y=int(input())
print(x+y)
emy_no=int(input())
emy_name=input()
emy_salry=float(input())
emy_add=input()
emy_married=boool(input())
k=input().split(",")
print((k))'''
l=[10,20,30]
sum_=0
for i in l:
    sum_+=int(i)
print(sum_)
#forms of prints
print("lucky \n kopuri")
print("lucky\tkopuri")
print("lucky"+"kopuri")#both arg should be same data type when we concatinate the values
a,b,c=10,29,22#using sep attribute
print(a,b,c)
print("hello",end=".....")#usinng end
print("world")
print(10,20,30,40,sep=":")
a,b,c=10,20,30  # formating str
print("a value is %i" %a)
print("a value is %i and b value is %i" %(a,b))