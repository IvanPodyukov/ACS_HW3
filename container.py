import random

from cartoon import Cartoon
from fiction import Fiction
from science import Science


# Класс контейнера
class Container:
    def __init__(self):
        self.store = []

    # Генерация рандомных фильмов в контейнере
    def RandomIn(self, number):
        for i in range(number):
            type_of_movie = random.randint(1, 3)
            if type_of_movie == 1:
                movie = Fiction()
            elif type_of_movie == 2:
                movie = Cartoon()
            else:
                movie = Science()
            movie.RandomIn()
            self.store.append(movie)
        pass

    # Запись информации о контейнере в файл
    def Write(self, ostream):
        ostream.write(f"Container is store {len(self.store)} movie:\n")
        for shape in self.store:
            shape.Write(ostream)
            ostream.write("\n")
        ostream.write(f"Summa of Quotients  = {self.SumOfQuotients()}\n")
        ostream.write(f"Average quotient  = {self.SumOfQuotients() / len(self.store)}\n")
        pass

    # Сумма значений общей функции всех фильмов в контейнере
    def SumOfQuotients(self):
        sum = 0
        for movie in self.store:
            sum += movie.Quotient()
        return sum

    # Дополнительная функция
    def DeleteElementsWithQuotientLessThanAverage(self):
        average = self.SumOfQuotients() / len(self.store)
        new_store = []
        for movie in self.store:
            if movie.Quotient() >= average:
                new_store.append(movie)
        self.store.clear()
        self.store = new_store
        pass
