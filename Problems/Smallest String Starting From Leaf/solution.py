import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        pass

obj = Solution()
#data = obj.smallestFromLeaf(root = [0,1,2,3,4,3,4])
#data = obj.smallestFromLeaf(root = [25,1,3,1,3,0,2])
data = obj.smallestFromLeaf(root = [2,2,1,None,1,0,None,0])
print(data)