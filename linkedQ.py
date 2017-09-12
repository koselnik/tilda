class LinkedQ():
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __str__(self):
        """Returns queue element as string"""
        return "LinkedQ Class"

    def put(self,newElement):
        """Puts new element last in queue"""
        tempVar = Node(newElement)
        if self.isEmpty():
          self.first = tempVar
          self.last = tempVar
        else:
          self.last.next = tempVar
          self.last = tempVar
        self.size += 1

    def get(self):
        """Gets and returns the first element in queue """
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
        if self.isEmpty():
            return None
        return self.first.value

    def all(self, first = True):
        if self.isEmpty():
            if first:
                return str("")
            return
        return str(self.get()) + str(self.all())

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self):
    return "NodeClass" + str(self.value)
