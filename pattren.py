#pattrens
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
#2
n=int(input())
for i in range(1,n+1):
    if i==n:
        print("+ "*i)
    else:
        print("* "*i)
#3
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()
#4
n=int(input())
for i in range(0,n+2):
    for j in range(0,i):
        print(n-j,end=" ")
    print()
for i in range(0,n+1):
    for j in range(0,n-i):
        print(n-j,end=" ")
    print()