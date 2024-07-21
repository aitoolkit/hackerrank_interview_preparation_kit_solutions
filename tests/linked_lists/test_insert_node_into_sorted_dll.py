from topics.linked_lists.insert_node_into_sorted_dll import DoublyLinkedList, DoublyLinkedListNode, sortedInsert, print_doubly_linked_list

def test_sortedInsert():
    test_llist = DoublyLinkedList()  # type: ignore
    test_llist_items = [1, 3, 4, 10]
    for d in test_llist_items:
        test_llist.insert_node(d)  # type: ignore
    
    test_data = 5
    llist_1 = sortedInsert(test_llist.head, test_data)  # type: ignore
    
    expected_llist = DoublyLinkedList()  # type: ignore
    expected_llist_items = [1, 3, 4, 5, 10]
    for d in expected_llist_items:
        expected_llist.insert_node(d)  # type: ignore
    
    assert llist_1.next.next.next.data == expected_llist.head.next.next.next.data  # type: ignore
    
    