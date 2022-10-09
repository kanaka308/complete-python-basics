from unicodedata import name


def greet(name):
    print(f'good morning, {name}')


#now only the above code can be imported as a module
if __name__ == '__main__':#this is the module from where module is run
    n = input('Enter a name\n')
    greet(n)
    print(greet('Kanaka')) 

    
