import pytest

from main import BooksCollector

@pytest.fixture() # фикстура, которая создает объект класса BookCollector
def setup_bookcollector():
    collector = BooksCollector()
    return collector