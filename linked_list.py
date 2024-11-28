#!/usr/bin/env python3

from typing import List

class NodeList:
    def __init__(self, val: int, nxt=None):
        self.val = val
        self.nxt = nxt

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        aux = self.head
        counter = 0
        while aux:
            if counter == index:
                return aux.val
            counter += 1
            aux = aux.nxt
        return -1

    def insertHead(self, val: int) -> None:
        node = NodeList(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.nxt = self.head
            self.head = node

    def insertTail(self, val: int) -> None:
        node = NodeList(val)
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.nxt = node
            self.tail = node

    def remove(self, index: int) -> bool:
        prev = None
        curr = self.head
        counter = 0
        while curr:
            if counter == index:
                if curr == self.head and curr == self.tail:
                    self.head = None
                    self.tail = None
                    return True
                if curr == self.head:
                    self.head = self.head.nxt
                    return True
                if curr == self.tail:
                    self.tail = prev
                    self.tail.nxt = None
                    return True
                nxt = curr.nxt
                prev.nxt = nxt
                return True
            counter += 1
            prev = curr
            curr = curr.nxt
        return False

    def getValues(self) -> List[int]:
        output = []
        aux = self.head
        while aux:
            output.append(aux.val)
            aux = aux.nxt
        return output


if __name__=="__main__":
    linkedlist = LinkedList()
    linkedlist.insertTail(4)
    linkedlist.insertTail(5)
    linkedlist.insertTail(6)
    linkedlist.insertTail(7)

    print(linkedlist.getValues())

    linkedlist.insertHead(3)
    linkedlist.insertHead(2)
    linkedlist.insertHead(1)
    linkedlist.insertHead(0)

    print(linkedlist.getValues())

    print(linkedlist.get(0))
    print(linkedlist.get(1))
    print(linkedlist.get(2))
    print(linkedlist.get(6))
    print(linkedlist.get(7))

    print("Removing...")

    print(linkedlist.remove(7))
    print(linkedlist.getValues())

    print(linkedlist.remove(0))
    print(linkedlist.getValues())

    print(linkedlist.remove(3))
    print(linkedlist.getValues())