import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: TreeNode) -> TreeNode:
        pass

obj = Solution()
#data = obj.reverseOddLevels(root = [2,3,5,8,13,21,34])
#data = obj.reverseOddLevels(root = [7,13,11])
data = obj.reverseOddLevels(root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2])
print(data)