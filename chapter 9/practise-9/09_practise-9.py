file1 = 'chapter 9/copy.txt'
file2 = 'chapter 9/this.txt'

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print('both files are identical')

else:
    print('both files are not identical')