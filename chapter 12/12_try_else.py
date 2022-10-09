try:
    i = int(input("Enter a number: "))
    c = 1/i

except Exception as e:
    print(e)

else: #this executes if try block is executed sucessfully
    print("sucessfully executed try")