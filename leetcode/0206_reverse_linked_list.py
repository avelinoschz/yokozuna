# 0206. Reverse Linked List

# https://leetcode.com/problems/reverse-linked-list/

# Easy

# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    prev = None
    while curr:
        temp_next = curr.next
        curr.next = prev
        prev = curr
        curr = temp_next
    return prev

# Here is reversing the pointing, to previous one
# e.g. If the nodes are 3 - 4 - none
# head=3 head.next=4 head.next.next=None
# now 4 will point to 3
# and 3 will point to None because is the new tail
# this part would end put like 4 - 3 - None
# until it reaches the top
def reverseListRecursive(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    
    if not head.next:
        return head
    
    new_head = reverseListRecursive(head.next)
    
    head.next.next = head
    head.next = None
    
    return new_head

# Did another try on 2026, which works, but it is not as readable as the original from 2024
def reverseListRecursive2(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    
    last = reverseList(head.next)
    if last is None:
        return head

    head.next.next = head
    head.next = None

    return last

# Testing
n4 = ListNode(4)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

current = n1
while current:
    print(current.val, end=" -> ")
    current = current.next
print()

result = reverseListRecursive(n1)
current = result
while current:
    print(current.val, end=" -> ")
    current = current.next
print()
