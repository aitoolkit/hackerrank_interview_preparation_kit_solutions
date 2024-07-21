
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
        self.head: DoublyLinkedListNode = None # type: ignore
        self.tail: DoublyLinkedListNode = None # type: ignore

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data) # type: ignore

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def sortedInsert(llist, data):
    new_node = DoublyLinkedListNode(data) # type: ignore
    
    current_node = llist
    print(current_node.data)
    if (current_node.data > new_node.data):
        new_node.next = current_node
        llist = new_node
        return llist
    
    while (current_node.next and (current_node.next.data < data)):
        current_node = current_node.next
    if not current_node.next:
        current_node.next = new_node
        return llist
    new_node.next = current_node.next
    current_node.next = new_node
    return llist
    

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input())

#     for t_itr in range(t):
#         llist_count = int(input())

#         llist = DoublyLinkedList()

#         for _ in range(llist_count):
#             llist_item = int(input())
#             llist.insert_node(llist_item)

#         data = int(input())

#         llist1 = sortedInsert(llist.head, data)

#         print_doubly_linked_list(llist1, ' ', fptr)
#         fptr.write('\n')

#     fptr.close()
