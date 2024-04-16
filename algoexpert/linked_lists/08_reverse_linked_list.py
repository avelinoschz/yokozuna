# Reverse Linked List

# https://www.algoexpert.io/questions/reverse-linked-list

# Hard

# Write a function that takes in the head of a Singly Linked List, reverses 
# the list in place (i.e., doesn't create a brand new list), and returns its 
# new head.

# Each `LinkedList` node has an integer `value` as well as a `next` node in 
# the list or to `None` / `null` if it's the tail of the list.

# You can assume that the input Linked List will always have at least one node; 
# in other words, the head will never be `None` / `null`.

# Sample Input
# head = 0 > 1 -> 2 → 3 →> 4 →> 5 // the head node with value 0

# Sample Output
# 5 → 4 → 3 → 2 → 1 → 0 // the new head node with value 5

# Optimal:
# O(n) time | O(1) space - where `n` is the number of nodes in the Linked List

# Didn't add any AlgoExpert solution, since the solution using iteration
# was basically the same. Recursion wasn't covered.

# -----------------------------------------------

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# iterative
# Time complexity: O(n)
# Space complexity: O(1)
def reverseLinkedList1(head):
    prev = None
    curr = head
    while curr:
        temp_next = curr.next
        curr.next = prev
        prev = curr
        curr = temp_next
    return prev

# recursive
# Time complexity: O(n)
# Space complexity: (n)
def reverseLinkedList2(head):
    if not head.next:
        return head

    new_head = reverseLinkedList2(head.next)
    
    head.next.next = head
    head.next = None
    
    return new_head
    
