# 21. Merge TWo Sorted Lists

# https://neetcode.io/problems/merge-two-sorted-linked-lists/question
# https://www.youtube.com/watch?v=XIdigk956u0

# Linked Lists

# Easy

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

# Example 1:

# Input: list1 = [1,2,4], list2 = [1,3,5]

# Output: [1,1,2,3,4,5]
# Example 2:

# Input: list1 = [], list2 = [1,2]

# Output: [1,2]
# Example 3:

# Input: list1 = [], list2 = []

# Output: []
# Constraints:

# 0 <= The length of the each list <= 100.
# -100 <= Node.val <= 100

# 1. Recursion
# Merging two sorted linked lists recursively works by always choosing the smaller head node of the two lists.
# Whichever list has the smaller value should appear first in the merged list.
# So we:

# - Pick the smaller node.
# - Recursively merge the rest of the lists.
# - Attach the result to the chosen node.
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity: O(n+m)
# Space complexity: O(n+m)
# Where n is the length of list1 and m is the length of list2.
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2



# 2. Iteration
# To merge two sorted linked lists iteratively, we build the result step-by-step.
# We keep a pointer (node) to the current end of the merged list, and at each step we choose the smaller head node from list1 or list2.

# Because the lists are already sorted, whichever head is smaller must come next in the merged list.
# We attach that node, move the pointer forward, and continue until one list is empty.
# Finally, we attach the remaining nodes from the non-empty list.

# Using a dummy node makes handling the head of the merged list simple and clean.

# Time complexity: O(n+m)
# Space complexity: O(1)
# Where n is the length of list1 and m is the length of list2.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next

# Neetcode previous iterative implementation from the Youtube video.
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next
