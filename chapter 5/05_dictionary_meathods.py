
a = {
    'a':'b',
    "c":'d',
    'e':'f',
    1:2
}
print(a.keys()) # gives keys as list

print(type(a.keys())) #it's type is keys

print(tuple(a.keys()))# gives keys as tuple
#you can convert it to any datastructure
print(a.values()) #returns the values as list

print(a.items()) #gives (key,value) for all contents of dictionary

a.update({ #Adds new values and keys
    100:1000,
    200:20000
})
print(a)

print(a.get(100)) #gets values of that key and returns none if key not found

