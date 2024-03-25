# 21. Merge TWo Sorted Lists

# https://leetcode.com/problems/merge-two-sorted-lists/

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by 
# splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print("None")

# This was my first try to solve it recursively. It is happy path, considering
# only equal lenght linked lists
def mergeTwoListsRecursive(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1.next and not list2.next:
        if list1.val < list2.val:
            list1.next = list2
            return list1
        else:
            list2.next = list1
            return list2
    
    remaining = mergeTwoListsRecursive(list1.next, list2.next)
    if list1.val < list2.val:
        list1.next = list2
        list2.next = remaining
        return list1
    else:
        list2.next = list1
        list1.next = remaining
        return list2
    
# Needed some help, looking for a bit solutions and then I write it on my own.
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = temp = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next
    temp.next = list1 or list2
    return dummy.next

l19 = ListNode(9)
l15 = ListNode(5, l19)
l12 = ListNode(2, l15)
list1 = ListNode(1, l12)

l27 = ListNode(7)
l26 = ListNode(6, l27)
l23 = ListNode(3, l26)
list2 = ListNode(1, l23)

print_linked_list(list1)
print_linked_list(list2)

result = mergeTwoListsRecursive(list1, list2)
print_linked_list(result)