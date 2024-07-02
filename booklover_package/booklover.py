import pandas as pd

class BookLover:

    def __init__(self, name:str, email:str, fav_genre:str, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name:str, rating:int):
        if self.num_books == 0:
            read_book = False
        else:
            read_book = self.has_read(book_name)

        if read_book == True:
            return f'{book_name} already in book list'
        else:
            new_book = pd.DataFrame({'book_name':[book_name], 'book_rating':[rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
            return f'{book_name} added to book list'

    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values

    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        fav_books = self.book_list[self.book_list['book_rating'] > 3]
        return fav_books

if __name__ == '__main__':
    #bl1 = BookLover('Tyler', 't@gmail.com', 'history')
    #print(bl1.add_book('Book 1', 3))
    #print(bl1.add_book('Book 2', 5))
    #print(bl1.book_list)
    #print(bl1.add_book('Book 1', 4))
    #print(bl1.has_read('Book 2'))
    #print(bl1.add_book('Book 3', 5))
    #print(bl1.num_books_read())
    #print(bl1.fav_books())
    pass


