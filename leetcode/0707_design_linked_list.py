# 707. Design Linked List

# https://leetcode.com/problems/design-linked-list/description/

# Design your implementation of the linked list. You can choose to use a singly 
# or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is 
# the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev 
# to indicate the previous node in the linked list. Assume all nodes in the linked 
# list are 0-indexed.

# Implement the MyLinkedList class:

# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the 
# index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the 
# linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in 
# the linked list. If index equals the length of the linked list, the node will be 
# appended to the end of the linked list. If index is greater than the length, the 
# node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the 
# index is valid.

# Example 1:
# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]

# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3

# Since I already did a singly linked list implementation in the neetcode platform
# I decided to implement a double linked list for this leetcode problem, since
# I already did an implementation of a sinlgy linked list in the neetcode course.
class ListNode:
    def __init__(self, val=0):
        self.val=val
        self.next=None
        self.prev=None

class MyLinkedList:

    def __init__(self):
        dummy_head = ListNode(-999)
        dummy_tail = ListNode(999)
        self.head = dummy_head
        self.tail = dummy_tail
        self.head.next = dummy_tail
        self.tail.prev = dummy_head
        
    def get(self, index: int) -> int:
        curr = self.head.next 
        i = 0
        while curr:
            if i == index:
                break
            curr = curr.next
            i += 1
        if not curr or curr == self.tail:
            return -1

        return curr.val

    def addAtHead(self, val: int) -> None:
        dummy = self.head
        new_node = ListNode(val)

        if dummy.next:
            dummy.next.prev = new_node

        new_node.next = dummy.next
        new_node.prev = dummy

        dummy.next = new_node

    def addAtTail(self, val: int) -> None:
        dummy = self.tail
        new_node = ListNode(val)
        
        if dummy.prev:
            dummy.prev.next = new_node
        
        new_node.prev = dummy.prev
        new_node.next = dummy
        
        dummy.prev = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                break
            curr = curr.next
            i += 1
        if not curr:
            return
        
        new_node = ListNode(val)
        new_node.prev = curr.prev
        new_node.next = curr

        curr.prev.next = new_node
        curr.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                break
            curr = curr.next
            i += 1
        if not curr or curr == self.tail:
            return

        curr.prev.next = curr.next
        curr.next.prev = curr.prev

    def print_doubly_linked_list(self):
        current = self.head
        while current:
            print(current.val, end=" <-> " if current.next else "")
            current = current.next
        print("None")


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

doubly_head = MyLinkedList()
doubly_head.addAtHead(2)
doubly_head.addAtHead(1)
doubly_head.addAtTail(5)
doubly_head.addAtTail(7)
doubly_head.print_doubly_linked_list()
got = doubly_head.get(2)
print("got at index 2:", got)
doubly_head.addAtIndex(3, 6)
print("add val 6 at index 3:")
doubly_head.print_doubly_linked_list()
print("delete at index 1:")
doubly_head.deleteAtIndex(1)
doubly_head.print_doubly_linked_list()
doubly_head.addAtIndex(70, 888)
print("add val 888 at index 4:")
doubly_head.print_doubly_linked_list()
got = doubly_head.get(5)
print("got at index 5:", got)
