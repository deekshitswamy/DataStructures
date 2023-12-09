import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        pass

obj = Solution()
#data = obj.inorderTraversal(root = [1,None,2,3])
#data = obj.inorderTraversal(root = [])
data = obj.inorderTraversal(root = [1])
print(data)