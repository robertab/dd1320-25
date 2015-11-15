from array import array


class ArrayQ():
    """
    Initierar det privata attributet array för bättre abstraktion. 
    """
    def __init__(self, unit_type="i"):
        self._array = array(unit_type)

    def enqueue(self, number):
        """
        Beroende på vilken ordning vi väljer i listan. insert/append
        """
        return self._array.insert(0, number) 

    def dequeue(self):
        """
        Använder pop för att ta bort det "första" i listan. Dvs det 
        första vi enqueuear 
        """
        return self._array.pop()#Pop last element in list

    def isEmpty(self):
        """
        Kollar om arrayn innehåller något element. 
        """
        if len(self._array) == 0:
            return True
        else:
            return False



        

