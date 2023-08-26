l=[1,2,3,4]
l.append(5)
print(l)
#extend
l=[1,2,3,4]
l.extend([5,6])
print(l)
#insert
l=[1,2,3,4]
l.insert(1,10)
print(l)
#pop(remove the element at the specifed index) and return the removed value
l=[1,2,3,4]
l.pop(1)
print(l)
#removes the first matching element (remove)
l=[1,2,3,4]
l.remove(1)
print(l)
#clear  used for removing all items from the List
l=[1,2,3,4]
l.clear()
print(l)
# index (it returns the index of given value)
l=[1,2,3,4,5,6,7]
print(l.index(6))
#sort
l=["lucky","nikki","apple","revathi"]
l.sort()