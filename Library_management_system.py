class Library:
    def __init__(self, listbooks):  
        self.books = listbooks

    def AvailableBooks(self):
        print("Books present:")
        for book in self.books:
            print("  " + book)

    def BorrowBook(self, bookName):
        if bookName in self.books:
            print(f"Book issued: {bookName}. Return the book within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Book is unavailable.")
            return False

    def ReturnBook(self, bookName):
        self.books.append(bookName)
        print("Issued book returned!")


class Student:
    def RequestBook(self):
        self.book = input("Enter the name of the book to borrow: ")
        return self.book

    def ReturnBook(self):
        self.book = input("Enter the name of the book to return: ")
        return self.book


if __name__ == "__main__":  
    clibrary = Library(["Python", "Java", "Php", "C++"])
    student = Student()
    while True:
        welcomemsg = '''\n...Welcome to Library Management System...
        Please choose an option below:
        1. View all books
        2. Request a book
        3. Return a book
        4. Exit
        ....'''
        print(welcomemsg)
        try:
            a = int(input("Enter a choice: "))
            if a == 1:
                clibrary.AvailableBooks()
            elif a == 2:
                clibrary.BorrowBook(student.RequestBook())
            elif a == 3:
                clibrary.ReturnBook(student.ReturnBook())
            elif a == 4:
                print("....Thanks!!...")
                exit()
            else:
                print("..Invalid choice!!..")
        except ValueError:
            print("Please enter a valid number.")
