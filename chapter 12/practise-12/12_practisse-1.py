def readFile(filename):


    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f'{filename} file not present')


readFile('chapter 9/sample.txt')
readFile('one.txt')