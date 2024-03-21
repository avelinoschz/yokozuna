class DynamicArray:
    
    def __init__(self, capacity: int):
        arr = []
        for i in range(0, capacity):
            arr.append(None)
        # self.arr = [0] * self.capacity

        self.arr = arr
        self.size = 0
        self.capacity = capacity
        

    def get(self, i: int) -> int:
        if i >= self.size:
            print("error out of index")
            return
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i >= self.size:
            print("error out of index")
            return
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size == 0:
            print("no elems in array")
            return
        pop = self.arr[self.size-1] 
        self.arr[self.size-1] = None
        self.size -= 1
        return pop
 
    def resize(self) -> None:
        doubled = []
        self.capacity = self.capacity * 2
        for i in range(0, self.capacity):
            doubled.append(None)
        # new_arr = [0] * self.capacity 

        for i in range(self.size):
            doubled[i] = self.arr[i]
        
        self.arr = doubled

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity

dynamo = DynamicArray(1)
print(dynamo)

print(dynamo.arr)
print("capacity:", dynamo.getCapacity())
print("size:", dynamo.getSize())

print("pushback 10")
dynamo.pushback(10)

print("capacity:", dynamo.getCapacity())
print("size:", dynamo.getSize())
print("get index 0:", dynamo.get(0))
print(dynamo.arr)

print("before resizing============")
print("pushback 20")
dynamo.pushback(20)

print(dynamo.arr)
print("capacity:", dynamo.getCapacity())
print("size:", dynamo.getSize())
print("get index 1:", dynamo.get(1))

print("before resizing============")
print("pushback 30")
dynamo.pushback(30)

print(dynamo.arr)
print("capacity:", dynamo.getCapacity())
print("size:", dynamo.getSize())
print("get index 2:", dynamo.get(2))


print("before popping============")
print("popback")
print(dynamo.popback())

print(dynamo.arr)
print("capacity:", dynamo.getCapacity())
print("size:", dynamo.getSize())
print("get index 2:", dynamo.get(1))


new_arr = [0] * 10
print(new_arr)