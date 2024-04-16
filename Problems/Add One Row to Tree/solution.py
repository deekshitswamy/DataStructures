import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        pass

obj = Solution()
#data = obj.addOneRow(root = [4,2,6,3,1,5], val = 1, depth = 2)
data = obj.addOneRow(root = [4,2,None,3,1], val = 1, depth = 3)
print(data)