
#
s1=input()
s2=input()
if(s1==s2):
    print("both same")
elif(s1>s2):
    print("s1 is big")
else:
    print("s2 is big")
#strip
city=input()
list=["gudivada","vijawavada","hyd","banglor"]
if city.strip() in list:
    print("ur city is availbe")
else:
    print("ur city is not vailable")
#find if var is not availble it returns -1
l="luckykopurilucky"
print(l.rfind(""))
print(l.find("a",5,9))
#index ....if var is not availble it returns value error
l="luckykopurilucky"
print(l.rindex(""))
print(l.index("a",5,9))
#finding sub string 
l="luckykopurilucky"
sub="l"
flag=False
pos=-1
while(True):
    pos=l.find(sub,pos+1,len(l))
    if(pos==-1):
        break
    print("found at index",pos)
    flag=True
if flag==False:
    print("not found")
#replace
s="lucky kopuri"
print(s)
s=s.replace("lucky","lakshmi")
print(s)
#split
s="lucky kopuri"
print(s.split())
s="lucky kopuri"
print(s.split())
k="20-11-2002"
l=k.split("-")
print(l)
for i in l:
    print(i)
#join
s="lucky kopuy"
k="-".join(s)
print(k)
#
k="lucKY kopuri"
print(k.upper())
print(k.lower())
print(k.swapcase())
print(k.capitalize())
print(k.title())