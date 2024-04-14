import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        pass

obj = Solution()
#data = obj.sumOfLeftLeaves(root = [3,9,20,null,null,15,7])
data = obj.sumOfLeftLeaves(root = [1])
print(data)