num = int(input("Enter your number\n"))
prime = False
for i in range(2,num):
    if(num%i == 0):
        prime=True
        break
if prime:
    print('Not Prime')
else:
    print('Prime')



    
    
