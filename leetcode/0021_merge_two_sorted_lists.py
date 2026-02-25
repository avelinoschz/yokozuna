# 21. Merge TWo Sorted Lists

# https://leetcode.com/problems/merge-two-sorted-lists/

# Easy

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

# Iterative solution
# Time complexity: O(n+m)
# Space complexity: O(1)
# Where n is the length of list1 and m is the length of list2.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = temp = ListNode()

        while list1 or list2:
            if not list1:
                temp.next = list2
                break
            elif not list2:
                temp.next = list1
                break
            elif list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            elif list2.val < list1.val:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        return dummy_head.next


# Recursive solution
# Time complexity: O(n+m)
# Space complexity: O(n+m)
# Where n is the length of list1 and m is the length of list2. 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        elif list1 == None and list2 == None:
            return None

        head = None
        if list1.val <= list2.val: 
            head = list1
            head.next = self.mergeTwoLists(list1.next, list2)
            
        elif list2.val < list1.val: 
            head = list2
            head.next = self.mergeTwoLists(list1, list2.next)

        return head


# ----------------------------------------------------------------------------------------------------
# Above are all 2024 

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
# only equal length linked lists
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

# Another round of recursive implementation. After looking this other solution: https://www.youtube.com/watch?v=bdWOmYL5d1g
    
# How this works, is that we compare the head of both lists, and we pick the smaller one, 
# and then we recursively call the function with the next node of the smaller list and the head of the other list. 
# This way we are always comparing the heads of the two lists, and we are building the merged list by attaching the smaller node to the result of the recursive call.

# e.g this two lists:
# 1 -> 2 -> 9 -> None
# 1 -> 3 -> 6 -> 7 -> None

# The recursive calls will be from end to start, and the result of the recursive call will be a sorted list with the remaining nodes, and we will attach the smaller node to the front of that list.
# 9
# 7 -> 9
# 6 -> 7 -> 9
# 3 -> 6 -> 7 -> 9
# 2 -> 3 -> 6 -> 7 -> 9
# 1 -> 2 -> 3 -> 6 -> 7 -> 9
# 1 -> 1 -> 2 -> 3 -> 6 -> 7 -> 9
def mergeTwoListsRecursively(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
        return list2
    elif not list2:
        return list1
    
    if list1.val < list2.val:
        list1.next = mergeTwoListsRecursively(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoListsRecursively(list1, list2.next)
        return list2
    
# Needed some help, looking for an iterative solution and then I wrote it on my own.
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