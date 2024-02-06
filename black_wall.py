from main import BooksCollector

import pytest
setup_bookcollector = BooksCollector()
setup_bookcollector.add_new_book('Мастер')
setup_bookcollector.set_book_genre('Мастер', 'Ужасы')
print(setup_bookcollector.books_genre)

print(setup_bookcollector.get_book_genre("Мастер"))