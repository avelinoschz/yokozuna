# Design Binary Search Tree

# Design a Binary Search Tree class.

# You will design a Tree Map, which maps an integer key to an integer value. 
# Your Tree class should support the following operations:

# TreeMap() will initialize an binary search tree map.
# void insert(int key, int val) will map the key to the value and insert it into the tree.
# int get(int key) will return the value mapped with the key. If the key is not present in the tree, return -1.
# int getMin() will return the value mapped to the smallest key in the tree. If the tree is empty, return -1.
# int getMax() will return the value mapped to the largest key in the tree. If the tree is empty, return -1.
# void remove(int key) will remove the key-value pair with the given key from the tree.
# int[] getInorderKeys() will return an array of the keys in the tree in ascending order.
# Note:

# The tree should be ordered by the keys.
# The tree should not contain duplicate keys. If the key is already present in the tree, 
# the original key-value pair should be overridden with the new key-value pair.

# Example 1:
# Input:
# ["insert", 1, 2, "get", 1, "insert", 4, 0, "getMin", "getMax"]

# Output:
# [null, 2, null, 2, 0]

# Example 2:
# Input:
# ["insert", 1, 2, "insert", 4, 2, "insert", 3, 7, "insert", 2, 1, "getInorderKeys", "remove", 1, "getInorderKeys"]

# Output:
# [null, null, null, null, [1, 2, 3, 4], null, [2, 3, 4]]

# Binary Search Tree Node
from typing import List

class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

# Implementation for Binary Search Tree Map
class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if self.root == None:
            self.root = newNode
            return

        current = self.root
        while True:
            if key < current.key:
                if current.left == None:
                    current.left = newNode
                    return
                current = current.left
            elif key > current.key:
                if current.right == None:
                    current.right = newNode
                    return
                current = current.right
            else:
                current.val = val
                return

    def get(self, key: int) -> int:
        current = self.root
        while current != None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.val
        return -1

    def getMin(self) -> int:
        current = self.findMin(self.root)
        return current.val if current else -1

    # Returns the node with the minimum key in the subtree
    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        current = self.root
        while current and current.right:
            current = current.right
        return current.val if current else -1
    
    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    # Returns the new root of the subtree after removing the key
    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if curr == None:
            return None

        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if curr.left == None:
                # Replace curr with right child
                return curr.right
            elif curr.right == None:
                # Replace curr with left child
                return curr.left
            else:
                # Swap curr with inorder successor
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if root != None:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)
            