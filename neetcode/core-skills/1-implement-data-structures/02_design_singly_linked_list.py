from typing import List

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if index == 0 and self.head:
            return self.head.val
        
        i = 1
        cur = self.head
        while(cur != None):
            cur = cur.next
            if cur == None:
                return -1
                
            if index == i:
                return cur.val
            
            i += 1

        return -1

    def insertHead(self, val: int) -> None:
        new_head = Node(val)
        if self.head != None:
            cur_head = self.head
            self.head = new_head
            new_head.next = cur_head
        else:
            self.head = new_head

        if self.tail == None:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        if self.head == None:
            self.insertHead(val)
            return

        new_tail = Node(val)
        self.tail.next = new_tail
        self.tail = new_tail
        

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        
        if index == 0:
            self.head = self.head.next
            return True

        i = 1
        cur = self.head.next
        prev = self.head
        while cur != None:
            if index == i:
                prev.next = cur.next
                if cur == self.tail:
                    self.tail = prev
                return True

            cur = cur.next
            prev = prev.next
            i += 1

        return False

    def getValues(self) -> List[int]:
        values = []
        
        cur = self.head
        while(cur != None):
            values.append(cur.val)
            cur = cur.next
        
        return values
    
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

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
