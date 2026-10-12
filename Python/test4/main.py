class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f'Successfully borrowed: "{self.title}" by {self.author}')
        else:
            print(f'Sorry, "{self.title}" is already borrowed!')

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f'Successfully returned: "{self.title}", now available.')
        else:
            print(f'"{self.title}" was not borrowed.')

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Cruel prince", "Holly Black")
book3 = Book("1984", "George Orwell")

print("-Library Demonstration")

book1.borrow()
book2.borrow()

book1.return_book()

book3.borrow()
