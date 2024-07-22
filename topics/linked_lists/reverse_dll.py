import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data) # type: ignore

        if not self.head:
            self.head = node
        else:
            self.tail.next = node # type: ignore
            node.prev = self.tail


        self.tail = node


def reverse(llist):
    if llist is None:
        return None
    
    current = llist
    temp = None
    
    while current is not None:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev
    
    if temp is not None:
        llist = temp.prev
    
    return llist