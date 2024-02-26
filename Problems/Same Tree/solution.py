import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        pass

obj = Solution()
#data = obj.isSameTree(p = [1,2,3], q = [1,2,3])
#data = obj.isSameTree(p = [1,2], q = [1,null,2])
data = obj.isSameTree(p = [1,2,1], q = [1,1,2])
print(data)