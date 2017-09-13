# -*- coding: utf-8 -*-
from sys import stdin

# ----- classes LinkedQ and Node from other labs ---- #


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

    def all(self, first=True):
        """Returns a string with all values in the queue"""
        if self.isEmpty():
            if first:
                return str("")
            return
        return (str(self.get()) + str(self.all())).strip()


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node Class" + str(self.value)

# ------ formula processing functions ------ #


def readFormel(formula):
    # <formel>::= <mol> \n

    # all elements are queued
    formula = queue(formula)
    # send the queue formula to be processed
    syntax = readMol(formula)
    # return True if it is a correct formula, otherwise if there are errors it
    # will be caught
    return True


def readMol(mol, parenthesis=False):
    # <mol>   ::= <group> | <group><mol>

    # if we are expecting a parenthesis and if it is a parenthesis return it and
    # remove it
    if parenthesis and mol.peek() == ")":
        # returns parenthesis and removes it
        return mol.get()

    # send molecule to be divided into groups
    readGroup(mol)

    # it will iterate until there are no characters left in the list
    if not mol.isEmpty():
        return readMol(mol, parenthesis)
    # if mol is empty and we were expecting a parenthesis then raise error
    if parenthesis:
        raise (SyntaxError("Saknad högerparentes vid radslutet " + mol.all()))
    else:
        return True


def readGroup(group):
    # Check if it is a group and send it forward to required check mol, atom, num, etc
    # <group> ::= <atom> |<atom><num> | (<mol>) <num>

    # set the first element in queue to first
    first = group.get()

    # if it is a correct atom
    if readAtom(first, group):
        # Check if there is a number or if it is empty
        readNum(group, True)
        return

    # else if it is a parenthesis
    elif first == "(":
        if readMol(group, True) == ")":
            if not readNum(group, False):
                raise SyntaxError(
                    "Saknad siffra vid radslutet " + str(group.all()))
            return True

    # if isn't a valid atom or a parenthesis and it isn't empty then return
    # error
    if not group.isEmpty():
        raise SyntaxError(
            "Felaktig groupstart vid radslutet " + first + str(group.all()))


def readAtom(first, atom):
    # Check if it is an atom
    # <atom>  ::= <LETTER> | <LETTER><letter>
    # here is the list of the expected/"correct" atoms
    atoms = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F",
             "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"]

    second = ""
    # Check if the first element is is uppercase
    if first.isupper():
        if atom.peek().islower():
            second = atom.get()
        joinedElem = ("".join([first, second]))
        if joinedElem in atoms:
            return True
        else:
            raise SyntaxError("Okänd atom vid radslutet " + str(atom.all()))
    # if it is lowercase then it's incorrect, so raise an error
    elif first.islower():
        raise SyntaxError(
            "Saknad stor bokstav vid radslutet " + first + str(atom.all()))
    # otherwise it isn't a string so just return
    return


def readNum(num, numNotNecessary):
    # Check if there is a valid number, if the number is necessary
    # <num>   ::= 2 | 3 | 4 | ...

    # if num is empty, check if we don't need a number then it's okay,
    # otherwise raise error
    if num.isEmpty():
        if numNotNecessary:
            return True
        else:
            raise SyntaxError("Saknad siffra vid radslutet  " + str(num.all()))

    # if num isn't empty but it is zero then remove it from the list to raise
    # the correct error according to instructions
    if num.peek() == "0":
        # raise error if 0
        num.get()
        raise SyntaxError("För litet tal vid radslutet " + str(num.all()))

    # here we know that num isn't empty and then it isn't zero so we can
    # iterate through it. We set a new list numbers and a boolean iterateNum
    # While num isn't empty or it has an element that can be parse to int it
    # will iterate
    numbers = []
    iterateNum = True

    while iterateNum:
        try:
            int(num.peek())
            numbers.append(int(num.get()))
        except:
            iterateNum = False

    # if numbers has only one element and if it is 1, then raise error
    if len(numbers) == 1 and numbers[0] == 1:
        raise SyntaxError("För litet tal vid radslutet " + str(num.all()))
    # if there are items in numbers and they are not 1 then it's a correct
    # number
    if len(numbers) >= 1:
        return True
    # if the sum of ints in num is equal to 1 then we raise the correct error

    # if it comes all the way down here then it isn't a number
    return False


def queue(formula):
    # Set the formula elements in the queue
    q = Queue()
    # make the formula into a list so that we can iterate through it and set
    # every element in the queue
    formList = list(formula)
    for a in formList:
        q.put(a)
    return q


class SyntaxError(Exception):
    pass


# ----- main ----- #
# sets indata to input from user
indata = stdin.readline()

# while there is indata
while indata:
    # break if input is #
    if "#" in indata:
        break
    # while input is not #, continue
    try:
        # try to read the indata as a formula and if correct print message
        readFormel(indata)
        print("Formeln är syntaktiskt korrekt ")
    except SyntaxError as felet:
        # if it fails then return correct error message
        print(felet)
    indata = stdin.readline()
