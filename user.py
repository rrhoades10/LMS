class User:
    def __init__(self, name, library_id):
        self.name = name
        self.__library_id = library_id
        self.borrowed_books = [] # stores book objects - instances of the book class 

    def show_user_info(self):
        for book in self.books:
            print(book.title)