#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def insertNodeAtPosition(llist, data, position):
    # Write your code here
    newNode = SinglyLinkedListNode(data)
    if position == 0:
        newNode.next = llist
        return newNode

    current = llist

    for _ in range(position - 1):
        current = current.next
    
    newNode.next = current.next
    current.next = newNode
    return llist


# Helper function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()

# Example Usage:
head = SinglyLinkedListNode(1)
head.next = SinglyLinkedListNode(2)
head.next.next = SinglyLinkedListNode(3)

data = 4
position = 2

new_head = insertNodeAtPosition(head, data, position)
printLinkedList(new_head)
