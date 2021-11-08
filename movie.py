import random
import string


# Класс фильмов
class Movie:
    # Конструктор
    def __init__(self):
        self.year = 0
        self.name = ""

    # Случайная генерация фильма
    def RandomIn(self):
        self.year = random.randint(1950, 2021)
        letters = string.ascii_lowercase
        self.name = ''.join(random.choice(letters) for i in range(random.randint(5, 13)))
        pass

    # Считывание информации о фильме
    def ReadStrArray(self, strArray, i):
        pass

    # Запись информации о фильме в файл
    def Write(self, ostream):
        pass

    # Общая функция для всех типов фильмов
    def Quotient(self):
        return self.year / len(self.name)
