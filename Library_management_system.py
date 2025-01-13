class library:
    def _init_(self,listbooks):
        self.books=listbooks
    def Availablebooks(self):
            print("Books present:")
            for book in self.books:
                print("  "+ book)
    def borrowbook(self,bookName):   
        if bookName in self.books:
            print(f"Book issued {bookName}.Return book within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Book is unavailable")
            return False
    def returnbook(self, bookName):
         self.books.append(bookName)
         print("Issued book returned!")
class Student:
    def reqbook(self):
        self.book=input("Enter name of book(borrow):-")
        return self.book
    def returnbook(self):
        self.book=input("Enter name of book(returnbook):-")
        return self.book
if _name== "main_":
    clibrary=library(["Python","Java", "Php", "C++"])
    student=Student()
    while(True):
        welcomemsg='''\n...Welcome to Library Management System...
        Please choose an option below:
        1.All books
        2.Request a book
        3.Return a book
        4.Exit
        ....''' 
        print(welcomemsg)
        a=int(input("Enter a choice:"))
        if a==1:
           clibrary.Availablebooks()
        elif a==2:
           clibrary.borrowbook(student.reqbook())
        elif a==3:
           clibrary.returnbook(student.returnbook())
        elif a==4:
           print("....Thanks!!...")
           exit()
        else:
           print("..Invalid choice!!.. ")