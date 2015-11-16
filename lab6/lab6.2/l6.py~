# Author: Robert Åberg, Sara Ervik

atoms = ["H","He","Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"]

from sys import stdin
from sys import exit

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
    readGroup(q)
    if q.peek() == '\n':
        return
    if q.peek() == ')':
        return
    else:
        readMol(q)

def readGroup(q):
    if q.peek() == '(':
        q.dequeue()
        readMol(q)
        if q.peek() == '\n':
            raise Syntaxfel("Saknad högerparentes")
        if q.peek() == ')':
            q.dequeue()
            if isNum(q.peek(), q):
                readNum(q)
                return
            raise Syntaxfel("Saknad siffra")            
    readAtom(q)
    if not q.isEmpty():
        readNum(q)

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
        return
    raise Syntaxfel("Okänd atom")

def readNum(q):
    if isNum(q.peek(), q):
        first = q.peek()
        if first == '0':
            q.dequeue()
            raise Syntaxfel("För litet tal")
        if first == '1':
            q.dequeue()
            if q.peek() == None or not isNum(q.peek(), q):
                raise Syntaxfel("För litet tal")
        while isNum(q.peek(), q):
            q.dequeue()
            if q.isEmpty():
                return

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

def readFormula(mol):
    q = storeFormula(mol) 
    try:
        readMol(q)
        if not q.isEmpty():
            if q.peek() == ')':
                readMol(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        return str(fel) + " vid radslutet " + str(printQueue(q))

def main():
    while True:
        mol = stdin.readline()
        if '#' in mol:
            return False
        else:
            result = readFormula(mol)
            print(result)
    
if __name__ == '__main__':
    main()
