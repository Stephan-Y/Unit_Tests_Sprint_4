import pytest

class TestBooksCollector:


    def test_add_new_book_add_two_books(self, setup_bookcollector):

        setup_bookcollector.add_new_book('Гордость и предубеждение и зомби')
        setup_bookcollector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(setup_bookcollector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['', 'Ля комедия 2, или Совсем другая история с элементами большого искусства'])
    def test_add_new_book_add_two_inappropriate_book(self, setup_bookcollector, name):
        setup_bookcollector.add_new_book(name)
        assert len(setup_bookcollector.get_books_genre()) == 0

    def test_add_new_book_books_name_in_books_genre(self, setup_bookcollector):
        setup_bookcollector.add_new_book('Мастер и Маргарита')
        assert 'Мастер и Маргарита' in setup_bookcollector.get_books_genre()

    def test_set_book_genre_added_book(self, setup_bookcollector):
        setup_bookcollector.add_new_book('Мастер и Маргарита')
        setup_bookcollector.set_book_genre('Мастер и Маргарита', 'Проза')
        assert setup_bookcollector.get_book_genre("Мастер и Маргарита") == "Проза"

    @pytest.mark.parametrize('name', ['Гроздья гнева'])
    def test_get_books_with_specific_genre_get_specific_genre(self, setup_bookcollector, name):
        setup_bookcollector.add_new_book(name)
        setup_bookcollector.set_book_genre(name, 'Проза')
        setup_bookcollector.add_new_book('Мулан')
        setup_bookcollector.set_book_genre('Мулан', 'Мультфильмы')
        assert name in setup_bookcollector.get_books_with_specific_genre('Проза')

