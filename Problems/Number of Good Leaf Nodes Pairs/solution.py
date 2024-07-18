import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        pass

obj = Solution()
#data = obj.countPairs(root = [1,2,3,None,4], distance = 3)
#data = obj.countPairs(root = [1,2,3,4,5,6,7], distance = 3)
data = obj.countPairs(root = [7,1,4,6,None,5,3,None,None,None,None,None,2], distance = 3)
print(data)