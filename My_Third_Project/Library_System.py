class Library:
    def __init__(self,list_of_books):
        self.books_list = list_of_books
    def display_available_books(self):
        print("Books available in the Library:")
        for books in self.books_list:
            print("\n",books)
class Student:
    pass

if __name__=="__main_":
    lib = Library(["Eng","Math","Sci","Hist","Geo","Punjabi","Hindi"])
    lib.display_available_books()