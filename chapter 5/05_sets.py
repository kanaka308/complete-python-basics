a = {1,2,3,4,5,1,2} #Non repeatable collection of items
print(a)
print(type(a))

b = set() #This is an empty set
c = {} #This is an Empty Dictionary

#Adding Values
b.add(4)
b.add(9)
print(b)
#Sets are Hashable
# b.add([1,2,3]) #can't add list,tuple or dictionary as they are not hashable


print(len(b)) #gives length of set
b.remove(9)# removes an element
print(b)

b.pop() #removes a given item or removes random item if not given

print(b)

a.clear() #clears everything and makes it an empty set
a = {1,2,3,4}
b = {2,3,4,5}

print(a.union(b))#returns Union

print(a.intersection(b))#returns Intersection


