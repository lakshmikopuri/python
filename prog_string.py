
# Online Python - IDE, Editor, Compiler, Interpreter
n=input().split()
for i in range(1,len(n)+1):
    print(n[-i])
#eve nd odd positions
a=input()
eve=[]
odd=[]
for i in range(0,len(a)):
    if(i%2==0):
        eve.append(a[i])
    else:
        odd.append(a[i])
print(eve)
print(odd)
#even index
a=input()
print(a[::2])
#odd
a=input()
print(a[1::2])
#alpha order
a=input()
s1=s2=output=""
for x in a:
    if(x.isalpha()):
        s1+=x
    else:
        s2+=x
for x in sorted (s1):
    output+=x
for x in sorted(s2):
    output+=x
print(output)
#a4b2(ord,chr)
a=input()
output=""
for x in a:
    if(x.isalpha()):
        output+=x
        previous=x
    else:
        newchar= chr(ord(previous)+int(x))
        output+=newchar
print(output)
        
#
s1=input()
s2=input()
output=""
for i in range(0,len(s1)):
    output+=s1[i]+s2[i]
print(output)
#removing duplicts
a=input()
l=[]
for x in a:
    if x not in l:
        l.append(x)
output="".join(l)
print(output)
#couning char in given str
s=input()
d={}
for x in s:
    if x not in d.keys():
        d[x]=1
    else:
        d[x]+=1
print(d)