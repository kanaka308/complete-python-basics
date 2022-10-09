def remove_and_split(string, word):
    newStr = string.replace(word," ")
    return newStr.strip()
     

this = '      Shiva is good person'
n = remove_and_split(this, 'Shiva')

print(n) 