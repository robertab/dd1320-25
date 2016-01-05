# -*- coding: utf-8 -*-

""" 
Kurs:           DD1320/25 Tillämpad datalogi med Etik
Författare:     Robert Åbert
Uppgift:        Bank Queue
"""

class Node:
  def __init__(self, value, next=None):
    self.__value = value
    self.__next  = next
    
  def getValue(self): return self.__value
  
  def getNext(self): return self.__next

  def setValue(self, data): self.__value = data

  def setNext(self, pointer): self.__next = pointer


class LinkedQ:
  def __init__(self):
    self.first = None
    self.last  = None
    
  def enqueue(self, data):
    new_node = Node(data)
    if self.first == None:
      self.first = new_node
      self.last  = new_node
    else:
      self.last.setNext(new_node)
      self.last  = new_node

  def dequeue(self):
    first_in_line = self.first.getValue()
    self.first = self.first.getNext()
    return first_in_line


  def isEmpty(self):
    return self.first == None
