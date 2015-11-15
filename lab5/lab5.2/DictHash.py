""" 
Kurs: DD1320/25 Tillämpad datalogi med Etik
Författare: Robert Åbert, Sara Ervik, CDATE_2.
Uppgift: Lab5.2
"""

class DictHash():
    """Metoder för att hantera Hashtabell"""
    def __init__(self):
        self.dictionary = {}

    def store(self, key, data):
        self.dictionary[key] = data

    def search(self, key):
        return self.dictionary[key]

    def __getitem__(self, key):
        return self.dictionary[key]
