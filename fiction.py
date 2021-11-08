from movie import *
import string


# Класс игровых фильмов
class Fiction(Movie):
    # Конструктор
    def __init__(self):
        super().__init__()
        self.producer = ""

    # Считывание информации об игровом фильме
    def ReadStrArray(self, strArray, i):
        if i >= len(strArray) - 2:
            return 0
        self.name = strArray[i]
        self.year = int(strArray[i + 1])
        self.producer = strArray[i + 2]
        i += 3
        return i

    # Запись информации об игровом фильме в файл
    def Write(self, ostream):
        ostream.write(f"Fiction: year = {self.year}, name = {self.name}, "
                      f"producer = {self.producer}, quotient = {self.Quotient()}")
        pass

    # Случайная генерация игрового фильма
    def RandomIn(self):
        super().RandomIn()
        letters = string.ascii_lowercase
        self.producer = ''.join(random.choice(letters) for i in range(random.randint(5, 13)))
        pass
