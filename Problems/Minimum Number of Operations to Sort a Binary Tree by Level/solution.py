import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: TreeNode) -> int:
        pass

obj = Solution()
#data = obj.minimumOperations(root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10])
#data = obj.minimumOperations(root = [1,3,2,7,6,5,4])
data = obj.minimumOperations(root = [1,2,3,4,5,6])
print(data)