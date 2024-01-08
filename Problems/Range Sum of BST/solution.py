import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        s = 0
        def explore(root, low, high):
            nonlocal s
            if low<=root.val<=high:
                s += root.val
            if root.left and low<root.val:
                explore(root.left, low, high)
            if root.right and high>=root.val:
                explore(root.right, low, high)
        explore(root, low, high)
        return s

obj = Solution()
#data = obj.rangeSumBST(n = 1)
#data = obj.rangeSumBST(root = [10,5,15,3,7,None,18], low = 7, high = 15)
data = obj.rangeSumBST(root = [10,5,15,3,7,13,18,1,None,6], low = 6, high = 10)
print(data)