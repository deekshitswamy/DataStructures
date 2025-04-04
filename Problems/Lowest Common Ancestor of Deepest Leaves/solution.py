import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        pass

obj = Solution()
#data = obj.lcaDeepestLeaves(root = [3,5,1,6,2,0,8,None,None,7,4])
#data = obj.lcaDeepestLeaves(root = [1])
data = obj.lcaDeepestLeaves(root = [0,1,3,None,2])
print(data)