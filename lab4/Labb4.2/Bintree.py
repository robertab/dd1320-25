"""
Författare: Robert Åberg

"""

class Node:
    """
    Hjälpklass till Bintree med left respektive right attribut med
    tillhörande set/get samt ett attribut med nodens värde med
    set/get
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def getValue(self):
        return self.value

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setValue(self, data):
        self.value = data

    def setRight(self, left_pointer):
        self.right = left_pointer

    def setLeft(self, right_pointer):
        self.left = right_pointer


class Bintree:
    def __init__(self, root=None):
        self.root = root

    def put(self, newvalue):
        self.root = putta(self.root, newvalue)


    def write(self):
        skriv(self.root)
        print("\n")

    def __contains__(self, value):
        return finns(self.root, value)


def putta(rot, newvalue):
    if rot == None:
        return Node(newvalue)
    else:
        if newvalue < rot.value:
            if rot.left == None:
                rot.left = Node(newvalue)
            else:
                putta(rot.left, newvalue)
        else:
            if rot.right == None:
                rot.right = Node(newvalue)
            else:
                putta(rot.right, newvalue)
        return rot
                
    
def finns(rot, searched_value):
    if rot == None:
        return False
    if searched_value == rot.value:
        return True
    if searched_value < rot.value:
        return finns(rot.left, searched_value)
    if searched_value > rot.value:
        return finns(rot.right, searched_value)

def skriv(rot):
    if rot != None:
        skriv(rot.left)
        print(rot.value)
        skriv(rot.right)

        
