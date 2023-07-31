import pandas as pd

class BookLover:
    
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
    
    def add_book(self, book_name, book_rating):
        if book_name in list(self.book_list['book_name']):
            print("This book is already in the BookLover's book_list")
        else:
            assert (book_rating >= 1 and book_rating <=5), "Book rating must be between 1 and 5"
            assert isinstance(book_rating, int), "Book must be an integer"
            new_book = pd.DataFrame({
                                        'book_name': [book_name], 
                                        'book_rating': [book_rating]
                                    })
            self.num_books += 1
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
    
    def has_read(self, book_name):
        if book_name in list(self.book_list['book_name']):
            return True
        else:
            return False
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]