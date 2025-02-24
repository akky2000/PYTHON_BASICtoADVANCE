'''
Write a Library class with no_of_books and books as two instance variables. 
Write a program to create a library from this Library class and 
show how you can print all books,add a book and get the number of books using different methods.
 Show that your program doesnt persist the books after the program is stopped!
'''




class library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self,book_name):
        self.books.append(book_name)
        self.no_of_books += 1


    def get_no_of_books(self):
        return self.no_of_books
    
    def show_books(self):

        if self.no_of_books==0:
            print("No books in the library")
        else:
            print("Books in the library are:")
            for book in self.books:
                print(book)

if __name__ == "__main__":

    lib=library() #create a book instances

   #add books
    lib.add_book("Python")
    lib.add_book("Java")
    lib.add_book("C++")
    lib.add_book("C#")

    
   #show all books
    lib.show_books()
    print(f"Number of books in the library is: {lib.get_no_of_books()}")

    





    
   