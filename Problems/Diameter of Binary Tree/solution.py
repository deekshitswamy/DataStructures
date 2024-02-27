import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        pass

obj = Solution()
#data = obj.diameterOfBinaryTree(root = [1,2,3,4,5])
data = obj.diameterOfBinaryTree(root = [1,2])
print(data)