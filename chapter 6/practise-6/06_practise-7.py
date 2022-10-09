percentage = int(input('Enter your percentage: \n'))
if percentage >= 90:
    grade = 'Excellent'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 50:
    grade = 'D'

else:
    grade = 'F'

print('you are grade is ' + grade)