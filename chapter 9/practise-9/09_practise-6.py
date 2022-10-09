#Check whether a log file contains python in it


with open('chapter 9/log.txt') as f:
    content = f.read()

if 'python' in content.lower():
    print('Yes python is present')

else: 
    print('No python is not present')
