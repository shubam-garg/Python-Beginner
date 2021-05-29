class Library:
    def __init__(self,list_of_books):
        self.books_list = list_of_books

    def display_available_books(self):
        num=0
        print("Books available in the Library:")
        for books in self.books_list:
            print(f"  {num+1}",books)
            num += 1

    def book_issued(self,bookName):
        if bookName in self.books_list:
            print(f"{bookName} book is issued to you")
            self.books_list.remove(bookName)
            return True
        else:
            print(f"{bookName} is not available")
            return False

    def book_return(self,bookName):
        if bookName in self.books_list:
            print("already returned")
        else:
            self.books_list.append(bookName)
            print("Thanks for returning")
        
class Student:
    def __init__(self,list_of_books):
        self.books_list = list_of_books

    def bookrequest(self):
        self.book=input("Enter the number of the book you want to issue: ")
        return self.book

    def bookreturn(self):
        self.book=input("Enter the name of the book you have returned: ") 
        if self.book in self.books_list:
            return self.book
        else:
            print("This book do not belongs to this library")      

if __name__=="__main__":
    lib = Library(["Eng","Math","Sci","Hist","Geo","Punjabi","Hindi"])
    std = Student(["Eng","Math","Sci","Hist","Geo","Punjabi","Hindi"])
while (True):  
    print('''*****welcome to your new world*****
    Please press one option from below list 1,2,3 or 4:
    1. List of books
    2. Request a book
    3. Return a book
    4. Move out''')
    a = int(input("Enter the no. : "))
    if a==1:
        lib.display_available_books()
    elif a==2:
        lib.book_issued(std.bookrequest())
    elif a==3:
        lib.book_return(std.bookreturn())
    elif a==4:
        print("Thanks for visiting")
        break
    else:
        print("invalid number")