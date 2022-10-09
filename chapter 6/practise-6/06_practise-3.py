marks1 = float(input('Enter subject1 marks\n'))
marks2 = float(input('Enter subject2 marks\n'))
marks3 = float(input('Enter subject3 marks\n'))

if marks1 < 33 or marks2 < 33 or marks3 < 33:
    print('You are fail in one of subject')

elif (marks1+marks2+marks3)/3 < 40:
    print('You are fail due to low percentage')
else:
    print('Conragulations! you passed you got', (marks1+marks2+marks3)/3, '%')
