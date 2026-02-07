# Design Dynamic Array (Resizable Array)

# Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

# Your DynamicArray class should support the following operations:

# DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
# int get(int i) will return the element at index i. Assume that index i is valid.
# void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
# void pushback(int n) will push the element n to the end of the array.
# int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
# void resize() will double the capacity of the array.
# int getSize() will return the number of elements in the array.
# int getCapacity() will return the capacity of the array.
# If we call void pushback(int n) but the array is full, we should resize the array first.

# Example 1:
# Input:
# ["Array", 1, "getSize", "getCapacity"]

# Output:
# [null, 0, 1]

# Example 2:
# Input:
# ["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]

# Output:
# [null, null, 1, null, 2]

# Example 3:
# Input:
# ["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]

# Output:
# [null, 0, 1, null, 1, 1, null, 2, 2, 2, null, 3, 3, 1, 2]

# Note: The index i provided to get(int i) and set(int i) is guranteed to be greater than or equal to 0 and less than the number of elements in the array.
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