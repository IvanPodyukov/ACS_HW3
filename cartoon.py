from movie import *


# Класс мультфильмов
class Cartoon(Movie):
    # Конструктор
    def __init__(self):
        super().__init__()
        self.type_of_cartoon = ""

    # Считывание информации о мультфильме
    def ReadStrArray(self, strArray, i):
        if i >= len(strArray) - 2:
            return 0
        self.name = strArray[i]
        self.year = int(strArray[i + 1])
        type_of_cartoon = int(strArray[i + 2])
        if type_of_cartoon == 1:
            self.type_of_cartoon = "drawn"
        elif type_of_cartoon == 2:
            self.type_of_cartoon = "puppet"
        else:
            self.type_of_cartoon = "plasticine"
        i += 3
        return i

    # Запись информации о мультфильме в файл
    def Write(self, ostream):
        ostream.write(f"Cartoon: year = {self.year}, name = {self.name}, "
                      f"type of cartoon = {self.type_of_cartoon}, quotient = {self.Quotient()}")
        pass

    # Случайная генерация мультфильма
    def RandomIn(self):
        super().RandomIn()
        type_of_cartoon = random.randint(1, 3)
        if type_of_cartoon == 1:
            self.type_of_cartoon = "drawn"
        elif type_of_cartoon == 2:
            self.type_of_cartoon = "puppet"
        else:
            self.type_of_cartoon = "plasticine"
        pass
