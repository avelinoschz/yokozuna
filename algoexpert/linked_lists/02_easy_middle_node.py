# You're given a Linked List with at least one node. Write a function that 
# returns the middle node of the Linked List. If there are two middle nodes 
# (i.e. an even length list), your function should return the second of these nodes.

# Each `LinkedList` node has an integer `value` as well as a `next` node pointing 
# to the next node in the list or to `None` / `null` if it's the tail of the list.

# Sample Input
# linkedList = 2 -> 7→> 3 -→5

# Sample Output
# // The middle could be 7 or 3,
# 3 > 5 // we return the second middle node

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n + m) therefore: O(n) time | O(1) space
# `n` being the length of the linkedlist
# `m` being the half length of the linkedList
def middleNode_Algo1(linkedList):
    count = 0
    currentNode = linkedList
    while currentNode is not None:
        count += 1
        currentNode = currentNode.next

    middleNode = linkedList
    for _ in range(count // 2):
        middleNode = middleNode.next
    
    return middleNode

# O(n/2) therefore: O(n) time | O(1) space
def middleNode_Algo2(linkedList):
    slowNode = linkedList
    fastNode = linkedList

    while fastNode is not None and fastNode.next is not None:
        fastNode = fastNode.next.next
        slowNode =  slowNode.next
        
    return slowNode 

# -----------------------------------------------

# This was my first solution, implementing two iterations
# O(n + m) therefore: O(n) time | O(1) space
def middleNode(linkedList):
    length = 0
    cur = linkedList
    while cur:
        length += 1
        cur = cur.next

    half = (length // 2)
    
    mid = linkedList
    while half > 0:
        half -= 1
        mid = mid.next
    
    return mid

# After reading the hints, implemented a two pointer technique
# In my case I did it in a slightly different way.
# O(n + m) therefore: O(n) time | O(1) space
def middleNode(linkedList):
    fast = linkedList
    slow = linkedList

    while fast.next:
        slow = slow.next
        if fast.next.next:
            fast = fast.next.next
        else:
            break
    
    return slow

