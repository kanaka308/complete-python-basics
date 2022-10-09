try:
    i = int(input("Enter a number: "))
    c = 1/i

except Exception as e:
    print(e)
    exit()

finally: #this executes irrespective of try or except
    print("we are done")

print('thanks for using the program')#executes only if try blok is executed sucessfully
