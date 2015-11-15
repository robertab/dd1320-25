"""
Kurs: DD1320/25 Tillämpad datalogi med Etik
Författare: Robert Åbert, Sara Ervik, CDATE_2.
Uppgift: Lab5.1
"""

from search_and_sort import *
import timeit

def main():

    filename = "unique_tracks.txt"

    lista, dictionary = readfile(filename)
    n = len(lista)
    print("Antal element =", n)

    sista = lista[n-1]
    testartist = sista.artist

    linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 10)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

    sorttid = timeit.timeit(stmt = lambda: sortera(lista), number = 10)
    print("Sorteringen tog", round(sorttid, 4), "sekunder")

    bintid = timeit.timeit(stmt = lambda: binsok(lista, testartist), number = 10)
    print("Binärsökningen tog", round(bintid, 4) , "sekunder")

    dictionarytid = timeit.timeit(stmt = lambda: dictionary[testartist], number = 10)
    print("Slå upp i dictionary tog", round(dictionarytid, 4) , "sekunder")

if __name__ == '__main__':
    main()