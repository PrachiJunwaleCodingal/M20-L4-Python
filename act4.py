#Frozenset-

x = frozenset([10,20,30])
y = frozenset([20,30,40])

print(x.isdisjoint(y)) #check common elements 
print(x.difference(y))  #set1 that are not in set2.
print(x | y)  #elements from both x and y