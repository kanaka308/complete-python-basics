import os

oldname = "chapter 9/name.txt"

newname = "chapter 9/renamed.txt"

with open(oldname) as f:
    content = f.read()

with open(newname,'w') as f:
    f.write(content)

os.remove(oldname) #removes that file
