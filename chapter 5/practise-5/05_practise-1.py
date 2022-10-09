#Create dictionary of hidi words with values as their theie englis Translation

myDict = {
    "panka": 'fan',
    'dabba':'box',
    'vastu':'item'
}
print(myDict)
print("options are", myDict.keys())
a = input('Enter Hindi Word\n')
print('the meaning is:',myDict.get(a))