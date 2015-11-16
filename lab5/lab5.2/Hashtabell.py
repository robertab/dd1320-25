""" 
Kurs: DD1320/25 Tillämpad datalogi med Etik
Författare: Robert Åbert, Sara Ervik, CDATE_2.
Uppgift: Lab5.2
"""


"""Hjälpklass till Hashtabell"""
class HashNode:
    def __init__(self, key, value):
        self.key = key # låtnamn efter hashfuntion
        self.value = value # låtobjektet

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value


class Hashtabell:
    def __init__(self, size= 20000000):
        self.size =  size
        self.hashList = [None]*self.size

    def put(self, key, value): 
        hashIndex = hashfunction(key, self.size) # Sksapar ett index för objektet

        while self.hashList[hashIndex] != None:
            hashIndex = rehash(hashIndex, self.size)

        self.hashList[hashIndex] = HashNode(key, value) # Lägger till objektet i hashlistan på plats hashIndex


    def get(self, key):
        hashIndex = hashfunction(key, self.size)

        try: 
            while self.hashList[hashIndex] != None:

                if self.hashList[hashIndex].getKey() == key:
                    return self.hashList[hashIndex].getValue()
                else:
                    hashIndex = rehash(hashIndex, self.size)

        except KeyError:
            return False
 
def hashfunction(key, size):
    result = 0
    for letter in key:
        result = result*32 + ord(letter)

    return result%size

def rehash(prevHash, size):
    return (prevHash+1)%size


    

        
        
        
        
        
        

    
        
