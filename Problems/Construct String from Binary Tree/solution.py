import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root:TreeNode) -> str:
        pass

obj = Solution()
#data = obj.tree2str(root = [1,2,3,4])
data = obj.tree2str(root = [1,2,3,None,4])
print(data)