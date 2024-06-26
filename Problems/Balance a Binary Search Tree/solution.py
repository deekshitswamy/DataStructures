import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        pass

obj = Solution()
#data = obj.balanceBST(root = [1,None,2,None,3,None,4,None,None])
data = obj.balanceBST(root = [2,1,3])
print(data)