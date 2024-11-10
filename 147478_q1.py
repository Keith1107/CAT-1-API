


# book class
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrowed_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def returned_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({'Borrowed' if self.is_borrowed else 'Available'})"



# library member class
class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

#borrowing a book
    def borrow_a_book(self, book):
        if book.borrowed_book():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"{book.title} is already borrowed.Sorry Try Again later")


#returning a borrowed book
    def return_book(self, book):
        if book in self.borrowed_books and book.returned_book():
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{book.title} was not borrowed by {self.name}.")


#List of borrowed books
    def list_of_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has not borrowed any books.Sorry.")
        else:
            print(f"{self.name} has borrowed the following books.Here is the list of the books:")
            for book in self.borrowed_books:
                print(f"- {book.book_id}: {book.title}")




# return or borrow a book from the libraryy system4
if __name__ == "__main__":

    # books
    book1 = Book(1, "Sniper Road Killer", "Kendrick LJ")
    book2 = Book(2, "The River and the Source", "Margaret A. Ogola")
    book3 = Book(3, "How to Play Football", "Ten Hag")
    
    member1 = LibraryMember("Messi", "M001")
    member2=LibraryMember("Ronaldo","CR7")

    #main menu and getting user input
    while True:
        print("\nWelcome to Keith's Library Management System")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. List borrowed books")
        print("4. Exit")
        choice = input("Choose one option between 1-4: ")
        
        #checking choice
        if choice == '1':
            print("\nAvailable books:")
            for i, book in enumerate([book1, book2, book3], start=1):
                print(f"{i}. {book}")
            book_choice = int(input("Choose one book to borrow (1-3): "))
            
            if book_choice == 1:
                member1.borrow_a_book(book1)
            elif book_choice == 2:
                member1.borrow_a_book(book2)
            elif book_choice == 3:
                member1.borrow_a_book(book3)
            else:
                print("Invalid choice. Try Again")
        
        elif choice == '2':
            print("\nYour borrowed books:")
            if not member1.borrowed_books:
                print("You have no books to return.Thank you.")
            else:
                for i, book in enumerate(member1.borrowed_books, start=1):
                    print(f"{i}. {book}")
                book_choice = int(input(f"Choose one book to return (1-{len(member1.borrowed_books)}): "))
                
                if 1 <= book_choice <= len(member1.borrowed_books):
                    member1.return_book(member1.borrowed_books[book_choice - 1])
                else:
                    print("Invalid choice. Try again.")
        
        #List of all borrowedd books
        elif choice == '3':
            member1.list_of_borrowed_books()
        
        elif choice == '4':
            print("Quiting the system. See you again player!!!........")
            break
        else:
            print("Error: Invalid input. Please enter a number between 1 and 4. Thank you player!!!")
