# -*- coding: utf-8 -*-

""" 
Kurs: DD1320/25 Tillämpad datalogi med Etik
Författare: Robert Åbert, Sara Ervik, CDATE_2.
Uppgift: Lab2
"""

class Node:
    """
    Hjälpklass till LinkedQ som sparar nuvarande värde och nästa med privata argument
    """
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
    """
    Kö som använder klassen Node för att skapa en länkad lista som används som en kö
    """
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, data):
        """
        Lägger till input data sist i kön
        """
        new_node = Node(data)
o        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.setNext(new_node)
            self.last = new_node

    def dequeue(self):
        """
        Returnerar första värdet i kön
        """
        first_in_line = self.first.getValue()
        self.first = self.first.getNext()
        return first_in_line


    def isEmpty(self):
        """
        Undersöker om det finns ett första objekt, om inte är länkade listan tom
        """
        if self.first == None:
            return True
        else:
            return False
