import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        b_lover1 = BookLover('Conor','cfm5qc@virginia.edu','Sci-Fi')
        b_lover1.add_book('Dune',4)
        message1 = "Book not in list"
        self.assertTrue('Dune' in list(b_lover1.book_list['book_name']),message1)
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        b_lover2 = BookLover('Billy','bb0gh@virginia.edu','Sci-Fi')
        b_lover2.add_book('The Martian',4)
        b_lover2.add_book('The Martian',5)
        expected = 1
        actual = len(b_lover2.book_list[b_lover2.book_list['book_name']=='The Martian'])
        message2 = 'Number of books does not match expected amount'
        self.assertEqual(actual, expected, message2)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        b_lover3 = BookLover('Mark P','mgp2vb@virginia.edu','Non-Fiction')
        b_lover3.add_book("Liar's Poker",3)
        message3 = "Book not found in list"
        self.assertTrue(b_lover3.has_read("Liar's Poker"), message3)

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        b_lover4 = BookLover('Sarah','smb9ju@virginia.edu','Dystopian')
        b_lover4.add_book("Flash Boys",2)
        message4 = "Book was found in list. It is not supposed to be in the list"
        self.assertFalse(b_lover4.has_read("Liar's Poker"), message4)

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        b_lover5 = BookLover('George Kron','gjk4pq@virginia.edu','Multiple')
        b_lover5.add_book("Flash Boys",2)
        b_lover5.add_book("Liar's Poker",3)
        b_lover5.add_book('The Martian',5)
        b_lover5.add_book('Dune',4)
        expected = 4
        actual = int(b_lover5.num_books)
        message5 = 'Number of books does not match expected amount'
        self.assertEqual(actual, expected, message5)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        b_lover6 = BookLover('Conor','cfm5qc@virginia.edu','Sci-Fi')
        b_lover6.add_book("Flash Boys",2)
        b_lover6.add_book("Liar's Poker",3)
        b_lover6.add_book('The Martian',5)
        b_lover6.add_book('Dune',4)
        message6 = "There is a book with a score <= 3 in the favorite list."
        self.assertTrue(b_lover6.fav_books()['book_rating'].min() > 3, message6)

if __name__ == '__main__':

    unittest.main(verbosity=3)