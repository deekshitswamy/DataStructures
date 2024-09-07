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
        pass

obj = Solution()
#data = obj.isSubPath(head = [4,2,8], root = [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
#data = obj.isSubPath(head = [1,4,2,6], root = [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
data = obj.isSubPath(head = [1,4,2,6,8], root = [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
print(data)