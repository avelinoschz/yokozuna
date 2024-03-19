# Design a Singly Linked List class.

# Your LinkedList class should support the following operations:

# LinkedList() will initialize an empty linked list.
# int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
# void insertHead(int val) will insert a node with val at the head of the list.
# void insertTail(int val) will insert a node with val at the tail of the list.
# int remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
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

# In this implementation, i overcomplicated a little bit
# because i didn't want to use the dummy head technique
# which later learned is pretty common.
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index: int) -> int:
        values = self.getValues()
        if index >= self.size or index < 0:
            return -1

        return values[index]

    def insertHead(self, val: int) -> None:
        node = Node(val)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
            self.size += 1
            return
        
        node.next = self.head
        self.head = node
        self.size += 1

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
            self.size += 1
            return
        
        self.tail.next = node
        self.tail = node
        self.size += 1
        
    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size or self.size == 0:
            return False

        if index == 0:
            # 0 out of [1]
            if not self.head.next:
                self.head = None
                self.tail = None
                self.size = 0
                return True
            # 0 out of [0 1 2]
            else:
                self.head = self.head.next
                self.size -= 1
                return True

        # [2, 1, 3, 5]
        prev_node = None
        curr_node = self.head
        i = 0
        while curr_node and i < index:
            prev_node = curr_node
            curr_node = curr_node.next
            i += 1
        
        # 2 out of 0 1 2
        if not curr_node.next:
            prev_node.next = None
            self.tail = prev_node
            self.size -= 1
            return True
        
        # 1 out of 0 1 2
        prev_node.next = curr_node.next
        self.size -= 1

        return True

    def getValues(self) -> list[int]:
        if not self.head:
            return []
        
        values = [self.head.val]
        cur_node = self.head
        while(cur_node.next):
            cur_node = cur_node.next
            values.append(cur_node.val)

        return values

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


linked_list = LinkedList()
print(linked_list)
print(vars(linked_list))
if not LinkedList:
    print("empty indeed")


linked_list.insertTail(1)

print(vars(linked_list.head))
print(vars(linked_list.tail))
print("initial head and tail ^")

linked_list.insertHead(2)
linked_list.insertTail(3)

linked_list.insertHead(4)
linked_list.insertTail(5)

vals = linked_list.getValues()
print(vals)

print(vars(linked_list.head))
print(vars(linked_list.tail))
print("final head and tail ^")

print("index 99:", linked_list.get(99))
print("index -30:", linked_list.get(-30))
print("get index 3:",linked_list.get(3))


vals = linked_list.getValues()
print(vals)
print("size:", linked_list.size)

print("removed index -1?", linked_list.remove(-1))
print(linked_list.getValues())
print("removed index 0?", linked_list.remove(0))
print(linked_list.getValues())
print("new size:", linked_list.size)

print("removed index 3?", linked_list.remove(3))
print(linked_list.getValues())
print("new size:", linked_list.size)

print("removed index 1?", linked_list.remove(1))
print(linked_list.getValues())
print("final size:", linked_list.size)
