from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2


        #Была ошибка в образце в 21 строчке,исправил

        #Мои тесты:
    
        #1)Добавление книги.Негативные проверки.
    @pytest.mark.parametrize(
        'invalid_name',
        ['', 'Ревьюер,желаю тебе хорошего настроения,меньше работы,больше приятных и радостных моментов))))))', 'HelloHelloHelloHelloHelloHelloHelloHelloH'])     
    def test_add_new_book_negativ_test(self,invalid_name):
        book = BooksCollector()
        book.add_new_book(invalid_name)
        assert len(book.get_books_genre()) == 0

        #1.1)Проверка граничного значения в 40 символов
    def test_add_new_book_add_same_books(self):
        name = 'HelloHelloHelloHelloHelloHelloHelloHello'
        sameBooks = BooksCollector()
        sameBooks.add_new_book(name)
        sameBooks.add_new_book(name)
        assert len(sameBooks.get_books_genre()) == 1

        #2)Проверка, что нельзя добавить 2 одинаковые книги
    def test_add_new_book_add_same_books(self):
        name = 'Опасные связи'
        sameBooks = BooksCollector()
        sameBooks.add_new_book(name)
        sameBooks.add_new_book(name)
        assert len(sameBooks.get_books_genre()) == 1

        #3)Проверка, что можно установить жанр книги,если она добавлена в словарь и жанр есть в списке
    def test_set_book_genre_if_book_in_book_genre_and_genre_in_genre_list(self):
        book = BooksCollector()
        book.add_new_book('Опасные связи')
        book.set_book_genre('Опасные связи','Детективы')
        assert book.get_book_genre('Опасные связи') ==  'Детективы'

        #4)Проверка, что нельзя установить жанр книги, если его нет в списке жанров
    def test_set_book_genre_if_book_in_book_genre_and_genre_not_in_genre_list(self):
        book = BooksCollector()
        book.add_new_book('Опасные связи')
        book.set_book_genre('Опасные связи','Драма')
        assert book.get_book_genre('Опасные связи') ==  ''    

        #5)Проверка, что нельзя установить жанр книге, если она не добалена в словарь
    def test_set_book_genre_if_book_not_in_book_genre_and_genre_in_genre_list(self):
        book = BooksCollector()
        book.add_new_book('Опасные связи')
        book.set_book_genre('Мурзилка','Ужасы')
        assert book.get_book_genre('Мурзилка') is None

        #6)Проверка вывода списка книг с определенным жанром
    def test_get_books_with_specific_genre(self):
        book = BooksCollector()
        book.add_new_book('Опасные связи')
        book.add_new_book('Мурзилка')
        book.add_new_book('Что происходит?')
        book.set_book_genre('Опасные связи','Ужасы')
        book.set_book_genre('Мурзилка','Ужасы')
        book.set_book_genre('Что происходит?','Фантастика')
        expected_list =['Опасные связи', 'Мурзилка']
        assert book.get_books_with_specific_genre('Ужасы') == expected_list


        #7)Проверка вывода списка книг для детей
    def test_get_books_for_children(self):
        book = BooksCollector()
        book.add_new_book('Опасные связи')
        book.add_new_book('Мурзилка')
        book.add_new_book('Что происходит?')
        book.set_book_genre('Опасные связи','Ужасы')
        book.set_book_genre('Мурзилка','Ужасы')
        book.set_book_genre('Что происходит?','Фантастика')
        expected_list =['Что происходит?']
        assert book.get_books_for_children() == expected_list


        #8)Тест на добавление книги в избранное
    @pytest.mark.parametrize(
        'book_name',
        ['Опасные связи', 'Мурзилка', 'Что происходит?'])         
    def test_add_book_in_favorites(self,book_name):
        book = BooksCollector()
        book.add_new_book(book_name)
        book.add_book_in_favorites(book_name)
        assert book_name in book.favorites


        #8.1)Тест на добавление книги в избранное, если она не была довлена в списокколлекию книг        
    def test_add_book_in_favorites_if_book_nit_in_list(self):
        book = BooksCollector()
        book.add_book_in_favorites('Зеленая миля')
        assert 'Зеленая миля' not in book.favorites


        #9)Тест на удаление из избранного
    @pytest.mark.parametrize(
        'book_name',
        ['Опасные связи', 'Мурзилка', 'Что происходит?'])     
    def test_delete_book_from_favorites(self,book_name):
        book = BooksCollector()
        book.add_new_book(book_name)
        book.add_book_in_favorites(book_name)
        book.delete_book_from_favorites(book_name)
        assert book_name not in book.favorites