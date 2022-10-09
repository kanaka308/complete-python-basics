#========================Library Management System================================================




class library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayBooks(self):
        print('The available books of this library are: ')
        for book in self.books:
            print('* ' + book)

    def borrowBook(self):
        self.bookName = input("Enter the name of the book you want to borrow: ")
        if self.bookName in self.books:
            print(f'you have been issued {self.bookName} book, keep it safe. Have a great day ahead')
            self.books.remove(self.bookName)
        else:
            print(f'Sorry! *{self.bookName}* book is either unavailable or issued to someone else..., We will contact you when its available')
        

    def returnBook(self):
        self.bookName = input('Enter the name of the book you want to return: ')
        print(f'You have returned {self.bookName}. Thanks for choosing our library, have a great day ahead!...')

        self.books.append(self.bookName)


#*********************************************************************************


if __name__ =='__main__':



    
    CentralLibrary = library(['python','oops','dbms','CN'])
    

    welcome = '''=========Welcome to Central Library=========
    
            Please choose an option: 
            1. Listing all the books
            2. Request a book
            3. Return a book
            4. Exit
            '''

    print(welcome)

    while(True):

        a = int(input('Please an option to continue: '))
        if a == 1:
            CentralLibrary.displayBooks()

        elif a == 2:
            CentralLibrary.borrowBook()

        elif a ==3 :
            CentralLibrary.returnBook()
        elif a == 4:
            exit()

        else:
            print('Please choose a valid option...')


