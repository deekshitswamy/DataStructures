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
        if not p and not q: return True
        elif not p or not q: return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

obj = Solution()
#data = obj.isSameTree(p = [1,2,3], q = [1,2,3])
#data = obj.isSameTree(p = [1,2], q = [1,null,2])
data = obj.isSameTree(p = [1,2,1], q = [1,1,2])
print(data)