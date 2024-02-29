import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        pass

obj = Solution()
#data = obj.isEvenOddTree(root = [1,10,4,3,null,7,9,12,8,6,null,null,2])
#data = obj.isEvenOddTree(root = [5,4,2,3,3,7])
data = obj.isEvenOddTree(root = [5,9,1,3,5,7])
print(data)