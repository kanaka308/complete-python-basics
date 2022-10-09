with open('chapter 9/this.txt') as f:
    content = f.read()

with open("chapter 9/copy.txt", 'w') as f:
    f.write(content)
