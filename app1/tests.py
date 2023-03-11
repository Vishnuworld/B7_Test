from django.test import TestCase

# Create your tests here.
from .models import Author, Book


class BaseModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()
        cls.author = Author(name='hawking')
        cls.author.save()
        cls.first_book = Book(author=cls.author, name="short_history_of_time")
        cls.first_book.save()
        cls.second_book = Book(author=cls.author, name="long_history_of_time")
        cls.second_book.save()

class AuthorModelTestCase(BaseModelTestCase):
    def test_created_properly(self):  # OK
         self.assertEqual(self.author.name, 'hawking')  # True
         self.assertEqual(True, self.first_book in self.author.book_set.all()) # True

class BookModelTestCase(BaseModelTestCase):
    def test_created_properly(self):
        self.assertEqual(1, len(Book.objects.filter(name__startswith='long')))  # True