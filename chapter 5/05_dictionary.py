myDict = {

    "FirstName": "Shiva",#FirstName is Key Shiva is tha value
    "LastName": "kanaka"

}
print(myDict['FirstName']) #U can acess values by using their keys

# print(myDict['Shiva']) # u cannot acess key using values it throws an error

marks = {   #This is also valied
    "st1" : [1,2,3,4],
    "st2" :[3,4,6,8]

}
print(marks['st1'])

dic = { #dictionary can contain another dictionary also
    "dict1" : {"a":"z","b":"y"},
    "dict2" : {"1":"100","2":"99"}
}
print(dic['dict1'])#acessing dictionary inside of dictionary
print(dic['dict1']['a']) #acessing element inside of another dictionary inside main dictionary

#A dictionary doesn't have any order

#keys are the index
#No duplicate keys
dic['dict1'] = 'xyz'#change any values

print(dic['dict1'])
