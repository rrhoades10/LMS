class Genre:

    def __init__(self, name, description):
        self.genre_name = name
        self.genre_description = description
    


class Book(Genre):

    def __init__(self, book_stuff, genre_name, genre_description):
        super().__init__(genre_name, genre_description)
        self.book_stuff = book_stuff
