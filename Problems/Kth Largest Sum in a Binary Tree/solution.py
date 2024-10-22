import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        pass

obj = Solution()
#data = obj.kthLargestLevelSum(root = [5,8,9,2,1,3,7,4,6], k = 2)
data = obj.kthLargestLevelSum(root = [1,2,None,3], k = 1)
print(data)