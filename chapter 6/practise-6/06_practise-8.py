from typing import AnyStr


post = input('Enter post')
post.find('shiva') == True
if 'shiva' or 'SHIVA' in post:
    print('This post talks about you')
else:
    print('no')


