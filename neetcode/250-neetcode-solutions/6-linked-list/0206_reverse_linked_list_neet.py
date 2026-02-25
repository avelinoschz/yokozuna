# 206. Reverse Linked List

# Neetcode video solution
# https://www.youtube.com/watch?v=G0_I-ZF0S38

# Difficulty: Easy

# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Example 1:

# Input: head = [0,1,2,3]

# Output: [3,2,1,0]
# Example 2:

# Input: head = []

# Output: []
# Constraints:

# 0 <= The length of the list <= 1000.
# -1000 <= Node.val <= 1000

# 1. Recursion
# Reversing a linked list using recursion works by thinking in terms of "reverse the rest, then fix the pointer for the current node."
# When we recursively go to the end of the list, that last node becomes the new head.
# While the recursion unwinds, each node points backward to the one that called it.
# Finally, we set the original head's `next` to `null` to finish the reversal.

# This approach uses the call stack to naturally reverse the direction of the pointers.

# Time complexity: O(n)
# Space complexity: O(n)

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead

# 2. Iteration
# Reversing a linked list iteratively is all about flipping pointers one step at a time.
# We walk through the list from left to right, and for each node, we redirect its `next` pointer to point to the node behind it.

# To avoid losing track of the rest of the list, we keep three pointers:

# `curr` → the current node we are processing
# `prev` → the node that should come after `curr` once reversed
# `temp` → the original next node (so we don't break the chain)
# By moving these pointers forward in each step, we gradually reverse the entire list.
# When `curr` becomes `null`, the list is fully reversed, and `prev` points to the new head.

# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev