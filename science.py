from movie import *


# Класс документальных фильмов
class Science(Movie):
    # Конструктор
    def __init__(self):
        super().__init__()
        self.length_of_movie_in_minutes = 0

    # Считывание информации о документальном фильме
    def ReadStrArray(self, strArray, i):
        # должно быт как минимум два непрочитанных значения в массиве
        if i >= len(strArray) - 2:
            return 0
        self.name = strArray[i]
        self.year = int(strArray[i + 1])
        self.length_of_movie_in_minutes = int(strArray[i + 2])
        i += 3
        return i

    # Запись информации о документальном фильме в файл
    def Write(self, ostream):
        ostream.write(f"Science: year = {self.year}, name = {self.name}, "
                      f"length of movie in minutes = {self.length_of_movie_in_minutes}, quotient = {self.Quotient()}")
        pass

    # Случайная генерация документального фильма
    def RandomIn(self):
        super().RandomIn()
        self.length_of_movie_in_minutes = random.randint(30, 180)
        pass
