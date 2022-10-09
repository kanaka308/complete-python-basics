words = ['donkey', 'monkey', 'idiot', 'stupid']

with open('chapter 9/sample.txt') as f:
    content = f.read()
   
   
for word in words:
    content = content.replace(word, '#$%^@&*')
    with open('chapter 9/sample.txt', 'w') as f:
        f.write(content)

