# neetcode video solution
# https://www.youtube.com/watch?v=G0_I-ZF0S38

# Iterative sol
# Time complexity: O(n)
# Space complexity: O(1)
# In the original solutions, is done iteratively the same way as neet.

# Recursive sol
# Time complexity: O(n)
# Space complexity: O(n)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode):
    if not head:
        return None
    
    newHead = head
    if head.next:
        newHead = reverseList(head.next)
        head.next.next = head
    head.next = None

    return newHead

n6 = ListNode(6)
n5 = ListNode(5, n6)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
result = reverseList(n1)
current = result
while current:
    print(current.val, end=" -> ")
    current = current.next
print()