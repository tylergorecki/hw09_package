import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        bl1 = BookLover('Tyler', 'ttg6nx@virginia.edu', 'Mystery')
        bl1.add_book('Goosebumps', 3)
        self.assertTrue('Goosebumps' in bl1.book_list['book_name'].values)

    def test_2_add_book(self):
        bl1 = BookLover('Tyler', 'ttg6nx@virginia.edu', 'Mystery')
        bl1.add_book('Goosebumps', 3)
        bl1.add_book('Goosebumps', 4)
        expected = 1
        actual = bl1.book_list['book_name'].value_counts()['Goosebumps']
        self.assertEqual(expected, actual)

    def test_3_has_read(self):
        bl1 = BookLover('Tyler', 'ttg6nx@virginia.edu', 'Mystery')
        bl1.add_book('Goosebumps', 3)
        read = bl1.has_read('Goosebumps')
        self.assertTrue(read)

    def test_4_has_read(self):
        bl1 = BookLover('Tyler', 'ttg6nx@virginia.edu', 'Mystery')
        bl1.add_book('Goosebumps', 3)
        read = bl1.has_read('Moneyball')
        self.assertFalse(read)

    def test_5_num_books_read(self):
        bl1 = BookLover('Tyler', 'ttg6nx@virginia.edu', 'Mystery')
        bl1.add_book('Goosebumps', 3)
        bl1.add_book('Moneyball', 5)
        bl1.add_book('Cat in the Hat', 4)
        expected = 3
        actual = bl1.num_books_read()
        self.assertEqual(expected, actual)

    def test_6_fav_books(self):
        bl1 = BookLover('Tyler', 'ttg6nx@virginia.edu', 'Mystery')
        bl1.add_book('Goosebumps', 3)
        bl1.add_book('Moneyball', 5)
        bl1.add_book('Cat in the Hat', 4)
        fav_books = bl1.fav_books()
        fav_books_more_3 = (fav_books['book_rating'] > 3).all()
        self.assertTrue(fav_books_more_3)

if __name__ == '__main__':
    unittest.main(verbosity=3)


