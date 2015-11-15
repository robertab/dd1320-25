# -*- coding: utf-8 -*-

"""
Författare: Robert Åberg, Sara Ervik
Kurs:       DD1320/25
Uppgift:    Breddenförstsökning - visa vägen.

"""
from Bintree import Bintree
from linkedQFile import LinkedQ
from SolutionFound import SolutionFound
from ParentNode import ParentNode

svenska = Bintree()
gamla = Bintree()
q = LinkedQ()

def makechildren(startord):
    alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    gamla.put(startord.word)
    for i in range(len(startord.word)): # Varje element i startordet
        for j in alphabet: # Ersätter med varje bokstav i alfabetet
            newWord = list(startord.word)
            newWord[i] = j
            newWord = "".join(newWord)
            if newWord in svenska and newWord not in gamla:
                gamla.put(newWord)
                newNode = ParentNode(newWord)
                newNode.parent = startord
                q.enqueue(newNode)

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
    pnode = ParentNode(startord)
    q.enqueue(pnode)
    try:
        while not q.isEmpty():
            nod = q.dequeue()
            makechildren(nod)
            if nod.word == slutord:
                print("\nVägen från", startord, "är:")
                nod.writechain(nod) # Skriver ut kedjan till slutord
                raise SolutionFound(nod)
        print("Det finns ingen väg till", slutord)
    except SolutionFound as nod:
        print()

if __name__ == '__main__':
    main()
