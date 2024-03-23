# https://www.algoexpert.io/questions/remove-duplicates-from-linked-list

# You're given the head of a Singly Linked List whose nodes are in sorted order 
# with respect to their values. Write a function that returns a modified version 
# of the Linked List that doesn't contain any nodes with duplicate values. The 
# Linked List should be modified in place (i.e., you shouldn't create a brand 
# new list), and the modified Linked List should still have its nodes sorted with 
# respect to their values.

# Each `LinkedList` node has an integer `value` aswellas a `next` node pointing 
# to the next node in the list or to `None` / `null` if it's the tail of the list.

# Sample Input
# linkedList = 1 > 1 →> 3 →> 4 →> 4 -> 4 →> 5 → 6 →> 6 // the head node with value 1

# Sample Output
# 1 → 3 → 4 → 5 → 6// the head node with value 1

# -----------------------------------------------

# Complexity analysis
# O(n) time | O(1) space - where n is the number of nodes

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    curr = linkedList

    original = curr
    while curr:
        nxt = curr.next
        
        if nxt and curr.value != nxt.value:
            original.next = nxt
            original = nxt
        elif not nxt:
            original.next = None

        curr = curr.next
    
    return linkedList