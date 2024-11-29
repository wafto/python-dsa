#!/usr/bin/env python3

from typing import List

class DequeNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return self.head == None

    def append(self, value: int) -> None:
        node = DequeNode(value)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def appendleft(self, value: int) -> None:
        node = DequeNode(value)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        if self.head == self.tail:
            value = self.head.val
            self.head = None
            self.tail = None
            return value
        aux = self.head
        while aux:
            if aux.next == self.tail:
                value = aux.next.val
                aux.next = None
                self.tail = aux
                return value
            aux = aux.next
        return -1

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        if self.head == self.tail:
            value = self.head.val
            self.head = None
            self.tail = None
            return value
        value = self.head.val
        self.head = self.head.next
        return value

    def getValues(self) -> List[int]:
        output = []
        aux = self.head
        while aux:
            output.append(aux.val)
            aux = aux.next
        return output

if __name__=="__main__":
    deq = Deque()

    deq.appendleft(1)
    deq.appendleft(2)

    print(deq.getValues())

    print(deq.pop())
    print(deq.pop())