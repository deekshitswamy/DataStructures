import io
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        pass

obj = Solution()
#data = obj.averageOfSubtree(root = [4,8,5,0,1,null,6])
data = obj.averageOfSubtree(root = [1])
print(data)