
name = input('enter name\n')
datee = input("enter date\n")

letter = '''Dear <|NAME|>,
You are selected!

have a great day

thanks

Date <|DATE|>'''

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", datee)

print(letter)