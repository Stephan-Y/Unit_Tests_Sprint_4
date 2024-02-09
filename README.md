# QA_tests #
Покрываю юнит-тестами приложение BooksCollector.
Оно позволяет установить жанр книг и добавить их в избранное.

Для создания объекта класса BookCollector используется
конструкция @pytest.fixture. Она находится в файле conftest.py.

## Тесты.
Тесты находятся в файле tests.py

* test_add_new_book_add_two_books - проверяем добавление двух книг в словарь books_genre.
* test_add_new_book_add_two_inappropriate_book - проверяем пустой список books_genre, после добавления двух книг с 0 и <41 символами.
* test_add_new_book_books_name_in_books_genre -проверяем добавлена ли конкретная книга в словарь books-genre
* test_set_book_genre_added_book - проверяем добавленный жанр к книге
* test_get_books_with_specific_genre_get_specific_genre - проверяем добавленные жанры к книгам, по названию книги
* test_get_books_genre_add_books_with_genre - проверяем возвращает ли метод get_boks_genre словарь из книг и их жанров
* test_get_books_for_children_add_kids_genre - проверяем добавлена ли книга с жанром "Мультфильмы" в список книг, возвращаемых методом get_books_for_children
* test_book_in_favorites_add_book - проверяем, что определенная книга добавлена в избранное методом add_book_in_favorites
* test_delete_book_from_favorites_add_and_delete_book - проверяем, что метод delete_book_from_favorites, удаляет определенную книгу из избранного
* test_get_list_of_favorites_books_add_book_in_favorites - проверяем включена ли определенная книга в избранное, возращаемая маетодом get_list_of_favorites_books

### Тесты на инициализацию: ###
* test_initialization_books_genre_empty_dict - проверяем пустой словарь books_genre
* test_initialization_favorites_empty_list - проверяем пустой список favorites
* test_intialization_genre_check_the_list - проверяем значения в списке genre
* test_intialization_genre_age_rating_check_the_list - проверяем значения в списке genre_age_rating



**Запуск тестов выполняется командой:**

pytest -v tests.py

**Оценка покрытия выполняется командой:**

pytest --cov=main



