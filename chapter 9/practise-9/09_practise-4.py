with open('chapter 9/sample.txt') as f:
    content = f.read()

content = content.replace('donkey', '@$#%$#%$%')

with open('chapter 9/sample.txt', 'w') as f:
    f.write(content)