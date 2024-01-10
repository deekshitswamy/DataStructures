import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        pass

obj = Solution()
#data = obj.amountOfTime(root = [1], start = 1)
data = obj.amountOfTime(root = [1,5,3,None,4,10,6,9,2], start = 3)
print(data)