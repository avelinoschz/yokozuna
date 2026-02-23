# Design Singly Linked List

# Design a Singly Linked List class.

# Your LinkedList class should support the following operations:

# LinkedList() will initialize an empty linked list.
# int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
# void insertHead(int val) will insert a node with val at the head of the list.
# void insertTail(int val) will insert a node with val at the tail of the list.
# bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
# int[] getValues() return an array of all the values in the linked list, ordered from head to tail.
# Example 1:
# Input: 
# ["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]

# Output:
# [null, null, null, true, [0, 2]]

# Example 2:
# Input:
# ["insertHead", 1, "insertHead", 2, "get", 5]

# Output:
# [null, null, -1]

# Note: The index int i provided to get(int i) and remove(int i) is guaranteed to be greater than or equal to 0.


# First try, before looking at the solution. Remembered that there was an approach using a dummy, but forgot how to implement it. 
# So I went with the approach of keeping track of the head and tail, and then traversing the list to get or remove nodes. This is not the most efficient approach, but it works.
from typing import List

# class LinkedList:
    
#     def __init__(self):
#         self.head = None
#         self.tail = None
    
#     def get(self, index: int) -> int:
#         if index == 0 and self.head:
#             return self.head.val
        
#         i = 1
#         cur = self.head
#         while(cur != None):
#             cur = cur.next
#             if cur == None:
#                 return -1
                
#             if index == i:
#                 return cur.val
            
#             i += 1

#         return -1

#     def insertHead(self, val: int) -> None:
#         new_head = Node(val)
#         if self.head != None:
#             cur_head = self.head
#             self.head = new_head
#             new_head.next = cur_head
#         else:
#             self.head = new_head

#         if self.tail == None:
#             self.tail = new_head

#     def insertTail(self, val: int) -> None:
#         if self.head == None:
#             self.insertHead(val)
#             return

#         new_tail = Node(val)
#         self.tail.next = new_tail
#         self.tail = new_tail
        

#     def remove(self, index: int) -> bool:
#         if not self.head:
#             return False
        
#         if index == 0:
#             self.head = self.head.next
#             return True

#         i = 1
#         cur = self.head.next
#         prev = self.head
#         while cur != None:
#             if index == i:
#                 prev.next = cur.next
#                 if cur == self.tail:
#                     self.tail = prev
#                 return True

#             cur = cur.next
#             prev = prev.next
#             i += 1

#         return False

#     def getValues(self) -> List[int]:
#         values = []
        
#         cur = self.head
#         while(cur != None):
#             values.append(cur.val)
#             cur = cur.next
        
#         return values
    
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# Second try using a dummy head node. This is to handle the edge cases of an empty singly linked list.
class LinkedList:
    def __init__(self):
        dummy = ListNode(-1)
        self.head = dummy
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur:
            if index == i:
                return cur.val
            
            cur = cur.next
            i += 1
            
        return -1
        
    def insertHead(self, val: int) -> None:
        new_head = ListNode(val)
        prev_head = self.head.next
        
        new_head.next = prev_head
        self.head.next = new_head

        if self.tail == self.head:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0
        while cur.next:
            if i == index:
                if cur.next == self.tail:
                    cur.next = None
                    self.tail = cur
                    return True

                cur.next = cur.next.next
                return True
            
            cur = cur.next
            i += 1
        
        return False

    def getValues(self) -> List[int]:
        vals = []
        cur = self.head.next
        while cur:
            vals.append(cur.val)
            cur = cur.next

        return vals

class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

ll = LinkedList()

ll.insertTail(9)
print("---------")
print("ll.insertTail(9)")
print("values:", ll.getValues())
print("head:", ll.head.val)
print("tail:", ll.tail.val)

ll.insertHead(2)
print("---------")
print("ll.insertHead(2)")
print("values:", ll.getValues())
print("head:", ll.head.val)
print("tail:", ll.tail.val)

ll.insertHead(1)
print("---------")
print("ll.insertHead(1)")
print("values:", ll.getValues())
print("head:", ll.head.val)
print("tail:", ll.tail.val)

ll.remove(2)
print("---------")
print("ll.remove(2)")
print("values:", ll.getValues())
print("head:", ll.head.val)
print("tail:", ll.tail.val)

ll.insertHead(4)
print("---------")
print("ll.insertHead(4)")
print("values:", ll.getValues())
print("head:", ll.head.val)
print("tail:", ll.tail.val)

ll.insertTail(7)
print("---------")
print("ll.insertTail(7)")
print("values:", ll.getValues())
print("head:", ll.head.val)
print("tail:", ll.tail.val)

result = ll.get(0)
print("---------")
print("ll.get(0)")
print("values:", ll.getValues())
print("result:", result)
print("head:", ll.head.val)
print("tail:", ll.tail.val)

result = ll.get(2)
print("---------")
print("ll.get(2)")
print("values:", ll.getValues())
print("result:", result)
print("head:", ll.head.val)
print("tail:", ll.tail.val)