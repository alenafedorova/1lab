import doctest


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not title:
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        if not author:
            raise ValueError("Имя автора не может быть пустым")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def is_long_book(self) -> bool:
        """
        Проверяет, является ли книга длинной (более 500 страниц).

        :return: True, если книга длинная, иначе False

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.is_long_book()
        False
        """
        ...

    def read_page(self, page_number: int) -> str:
        """
        Читает страницу книги.

        :param page_number: Номер страницы для чтения
        :return: Содержимое страницы
        :raise ValueError: Если номер страницы выходит за пределы книги

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.read_page(10)  # Возвращает содержимое страницы 10
        """
        if not isinstance(page_number, int):
            raise TypeError("Номер страницы должен быть целым числом")
        if page_number <= 0 or page_number > self.pages:
            raise ValueError("Номер страницы должен быть в пределах книги")
        ...

    def get_total_pages(self) -> int:
        """
        Возвращает общее количество страниц в книге.

        :return: Количество страниц

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.get_total_pages()
        328
        """
        ...


class Stack:
    def __init__(self):
        """
        Создание и подготовка к работе объекта "Стек"

        Примеры:
        >>> stack = Stack()  # инициализация экземпляра класса
        """
        self.items = []

    def push(self, item: object) -> None:
        """
        Добавляет элемент в стек.

        :param item: Элемент для добавления

        Примеры:
        >>> stack = Stack()
        >>> stack.push(10)
        """
        ...

    def pop(self) -> object:
        """
        Удаляет и возвращает верхний элемент стека.

        :return: Удаленный элемент
        :raise IndexError: Если стек пуст

        Примеры:
        >>> stack = Stack()
        >>> stack.push(10)
        >>> stack.pop()
        10
        """
        ...

    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек.

        :return: True, если стек пуст, иначе False

        Примеры:
        >>> stack = Stack()
        >>> stack.is_empty()
        True
        """
        ...


class SocialNetwork:
    def __init__(self, name: str, users_count: int):
        """
        Создание и подготовка к работе объекта "Социальная сеть"

        :param name: Название социальной сети
        :param users_count: Количество пользователей

        Примеры:
        >>> network = SocialNetwork("Facebook", 2900000000)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название социальной сети должно быть строкой")
        if not name:
            raise ValueError("Название социальной сети не может быть пустым")
        self.name = name

        if not isinstance(users_count, int):
            raise TypeError("Количество пользователей должно быть целым числом")
        if users_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")
        self.users_count = users_count

    def add_user(self, count: int) -> None:
        """
        Добавляет пользователей в социальную сеть.

        :param count: Количество добавляемых пользователей
        :raise ValueError: Если количество добавляемых пользователей отрицательное

        Примеры:
        >>> network = SocialNetwork("Facebook", 2900000000)
        >>> network.add_user(1000000)
        """
        if not isinstance(count, int):
            raise TypeError("Количество пользователей должно быть целым числом")
        if count < 0:
            raise ValueError("Количество добавляемых пользователей не может быть отрицательным")
        ...

    def remove_user(self, count: int) -> None:
        """
        Удаляет пользователей из социальной сети.

        :param count: Количество удаляемых пользователей
        :raise ValueError: Если количество удаляемых пользователей отрицательное или превышает текущее количество пользователей

        Примеры:
        >>> network = SocialNetwork("Facebook", 2900000000)
        >>> network.remove_user(1000000)
        """
        if not isinstance(count, int):
            raise TypeError("Количество пользователей должно быть целым числом")
        if count < 0 or count > self.users_count:
            raise ValueError("Недопустимое количество удаляемых пользователей")
        ...

    def get_user_count(self) -> int:
        """
        Возвращает текущее количество пользователей в социальной сети.

        :return: Количество пользователей

        Примеры:
        >>> network = SocialNetwork("Facebook", 2900000000)
        >>> network.get_user_count()
        2900000000
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации