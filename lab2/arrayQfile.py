from array import array


class ArrayQ():
    def __init__(self, unit_type="i"):
        self._array = array(unit_type)

    def enqueue(self, number):
        return self._array.append(number)

    def dequeue(self):
        return self._array.pop(0)

    def isEmpty(self):
        if len(self._array) == 0:
            return True
        else:
            return False
