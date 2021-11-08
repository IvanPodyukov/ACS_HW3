import sys
import time

from extender import *


def errorMessage():
    print("Incorrect command line! You must write: python main <inputFileName> <outputFileName>"
          " or python main <number> <outputFileName>")
    exit()


# ----------------------------------------------
if __name__ == '__main__':
    container = Container()
    startTime = time.perf_counter()
    if len(sys.argv) == 3:
        outputFileName = sys.argv[2]
        if sys.argv[1].isdigit():
            number = int(sys.argv[1])
            if number < 1 or number > 10000:
                print(f"Incorrect number of figures = {number}. Set 0 < number <= 10000\n")
                exit()
            container.RandomIn(number)
        else:
            inputFileName = sys.argv[1]
            # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки
            try:
                ifile = open(inputFileName)
            except IOError:
                errorMessage()
            str = ifile.read()
            ifile.close()
            # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
            strArray = str.replace("\n", " ").split(" ")
            movieNum = ReadStrArray(container, strArray)
    else:
        errorMessage()
    print('==> Start')
    ofile = open(outputFileName, 'w')
    ofile.write("Filled container:\n")
    container.Write(ofile)
    ofile.write("\nChanged container:\n")
    container.DeleteElementsWithQuotientLessThanAverage()
    container.Write(ofile)
    ofile.close()
    print(f'==> Seconds: {time.perf_counter() - startTime}')
    print('==> Finish')
