
#for loop
n=int(input())
sum_=0
for i in range(1,n+1):
    sum_+=i
print(sum_)

#productof num
n=int(input())
product=1
for i in range(1,n+1):
    s=int(input())
    product=product*s
print(product)
    
#printing n integers
n=int(input())
for i in range(1,n+1):
    print(i)
#odd even
for i in range(1,20):
    if(i%2==0):
        print(i,"even num")
    else:
        print(i,"odd num")
    