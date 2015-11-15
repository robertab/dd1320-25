# -*- coding: utf-8 -*-

"""
Författare: Robert Åberg, Sara Ervik
Kurs:       DD1320/25
Uppgift:    Breddenförstsökning - visa vägen.
"""



from Bintree import Bintree
from linkedQFile import LinkedQ
from Klar import Klar

svenska = Bintree()
gamla = Bintree()
q = LinkedQ()

def makechildren(startord):
    alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    gamla.put(startord)
    for i in range(len(startord)): # Varje element i startordet
        for j in alphabet: # Ersätter med varje bokstav i alfabetet
            newWord = list(startord)
            newWord[i] = j
            newWord = "".join(newWord)
            if newWord in svenska and newWord not in gamla:
                gamla.put(newWord)
                q.enqueue(newWord)

def readfile():
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet in svenska:
                gamla.put(ordet) 
            else:
                svenska.put(ordet)             # in i sökträdet

def main():
    readfile()
    startord = input("Mata in startord: ")
    slutord = input("Mata in slutord: ")
    q.enqueue(startord)
    try:
        while not q.isEmpty():
            nod = q.dequeue()
            makechildren(nod)
            if nod == slutord:
                raise Klar(nod)
        print("Det finns ingen väg")
    except Klar as nod:
        print("Det finns en väg till", slutord)

if __name__ == '__main__':
    main()


