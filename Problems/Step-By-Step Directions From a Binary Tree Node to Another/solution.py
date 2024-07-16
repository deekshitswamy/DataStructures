import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        pass

obj = Solution()
#data = obj.getDirections(root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6)
data = obj.getDirections(root = [2,1], startValue = 2, destValue = 1)
print(data)