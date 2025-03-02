class Node:
    def __init__(self, data):
        self.data = data
        self.nextData = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, nextData):
        self.nextData = nextData

    def getNext(self):
        return self.nextData


class UnOrderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def search(self, item):
        current = self.head
        found = False

        while not current and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def size(self):
        current = self.head
        conut = 0
        while current is not None:
            conut += 1
            current = current.getNext()

        return conut

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        current = self.head
        pervious = None
        while current is not None:
            pervious = current
            current = current.getNext()
        temp = Node(item)
        pervious.setNext(temp)
        temp.setNext(current)

    def pop(self):
        current = self.head
        previous = None
        while current.getNext() is not None:
            previous = current
            current = current.getNext()
        if previous:
            previous.setNext(None)
        else:
            raise "空列表无法删除"

    def items(self):
        current = self.head
        result = []
        while current is not None:
            result.append(current.getData())
            current = current.getNext()
        return result


class OrderedList:


if __name__ == '__main__':
    mylist = UnOrderedList()
    mylist.add(1)
    mylist.add(3)
    mylist.add(5)
    mylist.add(7)

    print(mylist.items())

    mylist.append(4)
    print(mylist.items())

    mylist.pop()
    print(mylist.items())

    mylist.pop()
    print(mylist.items())
