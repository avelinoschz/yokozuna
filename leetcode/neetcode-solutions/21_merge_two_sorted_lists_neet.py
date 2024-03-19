# neetcode video solution
# https://www.youtube.com/watch?v=XIdigk956u0

from typing import Optional

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

# Time complexity: O(n + m)
# Space complexity: O(n + m)
# Recursive solution was taken from other site: https://www.youtube.com/watch?v=bdWOmYL5d1g
    
# How this works is that the result of the recursive call, is a head including a sorted list
# and since the evaluation is done before, this result is placed next to the lower value
# done in a reverse way.
# e.g this two lists:
# 1 -> 2 -> 9None
# 1 -> 3 -> 6 -> 7None
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

# Time complexity: O(n + m)
# Space complexity: O(1)
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

l19 = ListNode(9)
l12 = ListNode(2, l19)
list1 = ListNode(1, l12)

l27 = ListNode(7)
l26 = ListNode(6, l27)
l23 = ListNode(3, l26)
list2 = ListNode(1, l23)

print_linked_list(list1)
print_linked_list(list2)

result = mergeTwoListsRecursively(list1, list2)
print_linked_list(result)