# day 34
# Library Book Tracker (instance methods + class methods)
class Book:
    total_books = 0
    borrowed_books = 0

    def __init__(self, title):
        self.title = title
        self.is_borrowed = False
        Book.total_books += 1

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            Book.borrowed_books += 1
            print(f"{self.title} has been borrowed. ")
        else:
            print(f"{self.title} is already borrowed. ")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            Book.borrowed_books -= 1
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not borrowed.")

    @classmethod
    def get_library_status(cls):
        return f"Total books: {cls.total_books}, Borrowed: {cls.borrowed_books}"


b1 = Book("1984")
b2 = Book("Harry Potter")

b1.borrow()
b2.borrow()
b1.borrow()   # should fail safely

print(Book.get_library_status())

b1.return_book()
print(Book.get_library_status())
