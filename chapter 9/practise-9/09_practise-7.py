content = True
i = 1

with open('chapter 9/log.txt') as f:
    while content:
        content = f.readline()

        if 'python' in content.lower():
            print('Yes python is present')
            print(f'python is present in line {i}')
        i += 1

    
       

       
        


  