import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        pass

obj = Solution()
#data = obj.replaceValueInTree(root = [5,4,9,1,10,None,7])
data = obj.replaceValueInTree(root = [3,1,2])
print(data)