from extender import *


def ReadStrArray(container, strArray):
    arrayLen = len(strArray)
    i = 0  # Индекс, задающий текущую строку в массиве
    movieNum = 0
    while i < arrayLen:
        str = strArray[i]
        key = int(str)  # преобразование в целое
        if key == 1:  # признак игрового фильма
            i += 1
            movie = Fiction()
            i = movie.ReadStrArray(strArray, i)  # чтение игрового фильма с возвратом позиции за ним
        elif key == 2:  # признак мультфильма
            i += 1
            movie = Cartoon()
            i = movie.ReadStrArray(strArray, i)  # чтение мультфильма с возвратом позиции за ним
        elif key == 3:  # признак документального фильма
            i += 1
            movie = Science()
            i = movie.ReadStrArray(strArray, i)  # чтение документального фильма с возвратом позиции за ним
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных фильмов
            return movieNum
        # Количество пробелами фильмов увеличивается на 1
        if i == 0:
            return movieNum
        movieNum += 1
        container.store.append(movie)
    return movieNum
