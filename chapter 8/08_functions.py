marks = [100,95,99,86,78]
print((sum(marks)/500)*100)

def percentage(marks):
    return (((marks[0]+marks[1]+marks[2]+marks[3]+marks[4])/400)*100)

marks1 = [45,46,59,99,100]
percentage1 = percentage(marks1)
print(percentage1)
