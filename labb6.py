# -*- coding: utf-8 -*-


def readFormel(formula):
    # <formel>::= <mol> \n
    formula = queue(formula)
    syntax = readMol(formula)
    return True


def readMol(mol, parenthesis = False):
    # <mol>   ::= <group> | <group><mol>

    if parenthesis and mol.peek() == ")":
        # return parenthesis and removes it
        return mol.get()

    readGroup(mol)

    # it will iterate until there are no characters left in the list
    if not mol.isEmpty():
        return readMol(mol, parenthesis)
    if parenthesis:
        raise (SyntaxError("Saknad högerparentes vid radslutet " + mol.all()))
    else:
        return True


def readGroup(group):
    # Check if it is a group and send it forward to required check mol, atom, num, etc
    # <group> ::= <atom> |<atom><num> | (<mol>) <num>
    first = group.get()
    if readAtom(first, group):
        # Check if there is a number or if it is empty
        readNum(group, True)
        return
    elif first == "(":
        if readMol(group, True) == ")":
            if not readNum(group, False):
                raise SyntaxError(
                    "Saknad siffra vid radslutet " + str(group.all()))
            return True
    if not group.isEmpty():
        raise SyntaxError(
            "Felaktig groupstart vid radslutet " + first + str(group.all()))


def readAtom(first, atom):
    # Check if it is an atom
    # <atom>  ::= <LETTER> | <LETTER><letter>
    atoms = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F",
             "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"]
    second = ""
    if first.isupper():
        if atom.peek().islower():
            second = atom.get()
        joinedElem = ("".join([first, second]))
        if joinedElem in atoms:
            return True
        else:
            raise SyntaxError("Okänd atom vid radslutet " + str(atom.all()))
    elif first.islower():
        raise SyntaxError(
            "Saknad stor bokstav vid radslutet " + first + str(atom.all()))
    return


def readNum(num, numNotNecessary):
    # Check if there is a valid number, if the number is necessary
    # <num>   ::= 2 | 3 | 4 | ...

    if num.isEmpty():
        if numNotNecessary:
            return True
        else:
            raise SyntaxError("Saknad siffra vid radslutet  " + str(num.all()))

    if num.peek() == "0":
        # raise error if 0
        num.get()
        raise SyntaxError("För litet tal vid radslutet " + str(num.all()))

    # numbers körs över en whileloop som plockar alla element
    numbers = 0
    numbersPicks = True

    while numbersPicks:
        try:
            int(num.peek())
            numbers += int(num.get())
        except:
            numbersPicks = False
    if numbers > 1:
        return True
    if numbers == 1:
        raise SyntaxError("För litet tal vid radslutet " + str(num.all()))
    return False


def queue(formula):
    # Set the formula elements in the queue
    q = Queue()
    formList = list(formula)
    for a in formList:
        q.put(a)
    return q


class SyntaxError(Exception):
    pass


# LinkedQ from other labs
class Queue():

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __str__(self):
        """Returns queue element as string"""
        return "Queue Class"

    def put(self, newElement):
        """Puts new element last in queue"""
        tempVar = Node(newElement)
        if self.isEmpty():
            self.first = tempVar
        else:
            self.last.next = tempVar
        self.last = tempVar
        self.size += 1

    def get(self):
        """Gets and returns the first element in queue and sets the next value as first"""
        if self.isEmpty():
            return ""
        firstVal = self.first.value
        self.first = self.first.next
        self.size -= 1
        return firstVal

    def isEmpty(self):
        """Returns True while queue is empty"""
        return (self.first == None)

    def peek(self):
        """Returns value of the first element in queue"""
        return None if self.isEmpty() else self.first.value

    def all(self):
        """Returns value of the first element in queue"""
        return str("") if self.isEmpty() else str(self.get()) + str(self.all())


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node Class" + str(self.value)
