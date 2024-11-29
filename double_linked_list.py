#!/usr/bin/env python3

from typing import List

class ListNode:
    def __init__(self, val: int, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if not self.head or index < 0 or index > self.size:
            return -1
        counter = 0
        aux = self.head
        while aux:
            if counter == index:
                return aux.val
            counter += 1
            aux = aux.next
        return -1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == 0:
            return self.addAtHead(val)
        if index == self.size:
            return self.addAtTail(val)
        aux = self.head
        counter = 0
        while aux:
            if counter == index:
                node = ListNode(val, aux.prev, aux)
                aux.prev.next = node
                aux.prev = node
                self.size += 1
                return
            counter += 1
            aux = aux.next

    def deleteAtHead(self) -> None:
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        self.size -= 1

    def deleteAtTail(self) -> None:
        if not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        self.size -= 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size:
            return
        if index == 0:
            return self.deleteAtHead()
        if index == self.size - 1:
            return self.deleteAtTail()
        aux = self.head
        counter = 0
        while aux:
            if counter == index:
                aux.prev.next = aux.next
                aux.next.prev = aux.prev
                self.size -= 1
                return
            counter += 1
            aux = aux.next

    def getValues(self) -> List[int]:
        output = []
        aux = self.head
        while aux:
            output.append(aux.val)
            aux = aux.next
        return output

if __name__=="__main__":
    linkedlist = DoubleLinkedList()

    linkedlist.addAtTail(4)
    linkedlist.addAtTail(5)
    linkedlist.addAtTail(6)
    linkedlist.addAtTail(7)

    print(linkedlist.getValues())

    linkedlist.addAtHead(3)
    linkedlist.addAtHead(2)
    linkedlist.addAtHead(1)
    linkedlist.addAtHead(0)

    print(linkedlist.getValues())

    print(linkedlist.get(0))
    print(linkedlist.get(1))
    print(linkedlist.get(2))
    print(linkedlist.get(6))
    print(linkedlist.get(7))

    linkedlist.addAtIndex(1, 100)
    linkedlist.addAtIndex(7, 200)

    print(linkedlist.getValues())

    print("Removing...")

    linkedlist.deleteAtIndex(1)
    linkedlist.deleteAtIndex(6)

    print(linkedlist.getValues())

    linkedlist.deleteAtHead()
    linkedlist.deleteAtHead()

    print(linkedlist.getValues())

    linkedlist.deleteAtTail()
    linkedlist.deleteAtTail()

    print(linkedlist.getValues())
