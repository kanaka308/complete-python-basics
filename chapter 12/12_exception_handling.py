while(True):
    print("press q to quit")
    a = input('Enter a number: ')
    if a == 'q':
        break
    try:
        a = int(a)
        if a>6:
            print("You Entered a number greater than 6")

    except Exception as e:
        print(f'Your input resulted in an error:\n{e}')


print('Thanks for Playing')