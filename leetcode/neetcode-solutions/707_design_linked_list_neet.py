# 707. Design Linked List

# neetcode video solution
# https://www.youtube.com/watch?v=Wf4QhpdVFQo

class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.right = ListNode()
        self.left = ListNode()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1
    
    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.left.next, self.left
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtTail(self, val: int) -> None:
        node, next, prev = ListNode(val), self.right, self.right.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left
        while cur and index > 0:
            index -= 1
            cur = cur.next
        if cur and index == 0:
            node, next, prev = ListNode(val), cur, cur.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left
        while cur and index > 0:
            index -= 1
            cur = cur.next
        if cur and cur != self.right and index == 0:
            next, prev = cur.next, cur.prev
            prev.next = next
            next.prev = prev