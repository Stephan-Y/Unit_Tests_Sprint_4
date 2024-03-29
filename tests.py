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

    def test_get_book_genre_get_specific_book_genre(self, setup_bookcollector):
        setup_bookcollector.add_new_book('Гроздья гнева')
        setup_bookcollector.set_book_genre('Гроздья гнева', 'Проза')
        assert setup_bookcollector.get_book_genre('Гроздья гнева') == 'Проза'

    def test_get_books_with_specific_genre_get_specific_genre(self, setup_bookcollector):
        setup_bookcollector.add_new_book('Гроздья гнева')
        setup_bookcollector.set_book_genre('Гроздья гнева', 'Проза')
        assert 'Гроздья гнева' in setup_bookcollector.get_books_with_specific_genre('Проза')

    @pytest.mark.parametrize('name', [{"Гроздья гнева":"Проза", "Мулан":"Мультфильмы", "Пятница начинается в субботу":"Фантастика"}])
    def test_get_books_genre_add_books_with_genre(self, setup_bookcollector, name):
        setup_bookcollector.add_new_book("Гроздья гнева")
        setup_bookcollector.set_book_genre("Гроздья гнева","Проза")
        setup_bookcollector.add_new_book("Мулан")
        setup_bookcollector.set_book_genre("Мулан","Мультфильмы")
        setup_bookcollector.add_new_book("Пятница начинается в субботу")
        setup_bookcollector.set_book_genre("Пятница начинается в субботу", "Фантастика")
        assert setup_bookcollector.get_books_genre() == name

    def test_get_books_for_children_add_kids_genre(self, setup_bookcollector):
        setup_bookcollector.add_new_book("Мулан")
        setup_bookcollector.set_book_genre("Мулан", "Мультфильмы")
        assert "Мулан" in setup_bookcollector.get_books_for_children()

    def test_add_book_in_favorites_add_book(self, setup_bookcollector):
        setup_bookcollector.add_new_book("Гроздья гнева")
        setup_bookcollector.add_book_in_favorites("Гроздья гнева")
        assert "Гроздья гнева" in setup_bookcollector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_add_and_delete_book(self, setup_bookcollector):
        setup_bookcollector.add_new_book("Гроздья гнева")
        setup_bookcollector.add_book_in_favorites("Гроздья гнева")
        setup_bookcollector.delete_book_from_favorites("Гроздья гнева")
        assert "Гроздья гнева" not in setup_bookcollector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_add_book_in_favorites(self, setup_bookcollector):
        setup_bookcollector.add_new_book("Гроздья гнева")
        setup_bookcollector.add_book_in_favorites("Гроздья гнева")
        assert "Гроздья гнева" in setup_bookcollector.get_list_of_favorites_books()


    def test_initialization_books_genre_empty_dict(self, setup_bookcollector):
        assert setup_bookcollector.books_genre == {}

    def test_initialization_favorites_empty_list(self, setup_bookcollector):
        assert setup_bookcollector.favorites == []

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии', 'Проза'])
    def test_intialization_genre_check_the_list(self, setup_bookcollector, genre):
        assert genre in setup_bookcollector.genre

    def test_intialization_genre_age_rating_check_the_list(self, setup_bookcollector):
        for genre_with_rating in setup_bookcollector.genre_age_rating:
            assert genre_with_rating in setup_bookcollector.genre_age_rating