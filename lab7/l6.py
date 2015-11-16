# Author: Robert Åberg, Sara Ervik

atoms = ["H","He","Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"]

from molgrafik import *
from atomfil import *
from sys import stdin
from sys import exit

atomlista = skapaAtomlista()
hashtabell = lagraHashtabell(atomlista)

class Syntaxfel(Exception):
    pass

class Node:
    def __init__(self, value, next=None):
        self.__value = value
        self.__next = next

    def getValue(self):
        return self.__value

    def getNext(self):
        return self.__next

    def setValue(self, data):
        self.__value = data

    def setNext(self, pointer):
        self.__next = pointer

class LinkedQ:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.setNext(new_node)
            self.last = new_node

    def dequeue(self):
        first_in_line = self.first.getValue()
        self.first = self.first.getNext()
        return first_in_line

    def isEmpty(self):
        if self.first == None: return True
        else: return False

    def peek(self):
        return self.first.getValue()

#------ Huvudprogrammet ---------------#

def readMol(q):
    mol = readGroup(q)
    if q.peek() == '\n':
        return mol
    if q.peek() == ')':
        return mol
    else:
        mol.next = readMol(q)
        return mol

def readGroup(q):

    ruta = Ruta()

    if q.peek() == '(':
        q.dequeue()
        ruta.down = readMol(q)
        # SPARA molekylen vi läst, för att sedan multiplicera
        if q.isEmpty() or q.peek() == '\n':
            raise Syntaxfel("Saknad högerparentes")
        if q.peek() == ')':
            q.dequeue()
            if isNum(q.peek(), q):
                ruta.num = readNum(q)
                return ruta
            raise Syntaxfel("Saknad siffra")

    ruta.atom = readAtom(q)

    if isNum(q.peek(), q):
        ruta.num = readNum(q)
    return ruta

def readAtom(q):
    atom = q.peek()
    if isCap(atom):
        atom = q.dequeue()
        if not q.isEmpty() and isLower(q.peek()):
            atom = atom + q.dequeue()
    elif isLower(atom):
        raise Syntaxfel("Saknad stor bokstav")
    else:
        raise Syntaxfel("Felaktig gruppstart")
    if atom in atoms:
        return atom
    raise Syntaxfel("Okänd atom")

def readNum(q):
    numberList = ""
    if isNum(q.peek(), q):
        first = q.peek()
        if first == '0':
            q.dequeue()
            raise Syntaxfel("För litet tal")
        if first == '1':
            numberList += first
            q.dequeue()
            if q.peek() == None or not isNum(q.peek(), q):
                raise Syntaxfel("För litet tal")
        while isNum(q.peek(), q):
            numberList += q.dequeue()
        return int(numberList)

def isCap(letter):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
    if letter in letters:
        return True
    return False

def isLower(letter):
    letters = 'abcdefghijklmnopqrstuvxyz'
    if letter in letters:
        return True
    return False

def isNum(letter, q):
    try:
        num=int(letter)
        return True
    except ValueError:
        return False

def storeFormula(mol):
    q = LinkedQ()
    for character in mol:
        q.enqueue(character)
    q.enqueue('\n')
    return q

def printQueue(q):
    string = ''
    while not q.isEmpty():
        character = q.dequeue()
        if character != '\n':
            string += character
    return string

def readFormula(q):
    mol = readMol(q)
    if not q.isEmpty():
        if q.peek() == ')':
            mol = readMol(q)
    return mol

def calculateWeight(ruta):
    if ruta != None:
        if ruta.down != None:
            vikt = (ruta.num * calculateWeight(ruta.down))
        else:
            vikt = ruta.num * hashtabell.get(ruta.atom).vikt 
        return vikt + calculateWeight(ruta.next)
    return 0

def main():
    try:
        while True:
            mg = Molgrafik()
            formel = stdin.readline()
            if '#' in formel:
                return False
            else:
                q = storeFormula(formel)
                result = readFormula(q)
                vikt = calculateWeight(result)
                print("Vikten av formeln är:", vikt)
                mg.show(result)

    except Syntaxfel as fel:
        return str(fel) + " vid radslutet " + str(printQueue(q))        

if __name__ == '__main__':
    result = main()
    print(result) # Skriver ut felmeddelandet

