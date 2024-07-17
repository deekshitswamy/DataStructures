import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        pass

obj = Solution()
#data = obj.delNodes(root = [1,2,3,4,5,6,7], to_delete = [3,5])
data = obj.delNodes(root = [1,2,4,None,3], to_delete = [3])
print(data)