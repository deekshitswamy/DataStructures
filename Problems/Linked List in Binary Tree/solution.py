import io
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if root is None:
            return False  # Base case: If the tree node is null, return false
        # Check if the head of the list matches the current tree node and continues matching
        if head.val == root.val and self.isNext(head, root):
            return True
        # Recursively check the left and right subtrees for a matching subpath
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def isNext(self, head: ListNode, root: TreeNode) -> bool:
        if head is None:
            return True  # If the linked list is fully matched, return true
        if root is None or head.val != root.val:
            return False  # If tree node is null or values don't match, return false
        # Continue checking the next node in the linked list with the left or right child of the current tree node
        return self.isNext(head.next, root.left) or self.isNext(head.next, root.right)

obj = Solution()
#data = obj.isSubPath(head = [4,2,8], root = [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
#data = obj.isSubPath(head = [1,4,2,6], root = [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
data = obj.isSubPath(head = [1,4,2,6,8], root = [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
print(data)