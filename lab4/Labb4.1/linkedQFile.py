""" 
Kurs: DD1320/25 Tillämpad datalogi med Etik
Författare: Robert Åbert, Sara Ervik, CDATE_2.
Uppgift: Lab2
"""

class Node:
	"""Hjälpklass till LinkedQ som sparar nuvarande värde och nästa med privata argument"""
	def __init__(self, value, next=None):
		self._value = value
		self._next = next


class LinkedQ:
	"""Kö som använder klassen Node för att skapa en länkad lista som används som en kö"""
	def __init__(self):
		self.first = None
		self.last = None

	def enqueue(self, data):
		"""Lägger till input data sist i kön"""
		NewNode = Node(data)
		if self.first == None:

			self.first = NewNode
			self.last = NewNode

		else:
			self.last._next = NewNode 
			self.last = NewNode
			

	def dequeue(self):
		"""Returnerar första värdet i kön"""
		first_in_line = self.first._value
		self.first = self.first._next
		return first_in_line


	def isEmpty(self):
		"""Undersöker om det finns ett första objekt, om inte är länkade listan tom"""
		if self.first == None:
			return True
		else:
			return False

		
		