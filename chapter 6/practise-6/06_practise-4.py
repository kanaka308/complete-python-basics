comment = input('Enter the text\n')
if('make alot of money' in comment):
    spam = True
elif('buy now' in comment):
    spam = True
elif('click this link' in comment):
    spam = True
elif('subscribe this' in comment):
    spam = True

else:
    print('Not a spam')

if (spam == True):
    print('THis is a spam')
else:
    print('this is not spam')




