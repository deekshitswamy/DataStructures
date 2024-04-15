import io
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        pass

obj = Solution()
#data = obj.sumNumbers(root = [1,2,3])
data = obj.sumNumbers(root = [4,9,0,5,1])
print(data)