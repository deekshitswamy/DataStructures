import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        # If both nodes are None, trees are equivalent.
        if not root1 and not root2:
            return True
        # If one node is None or values don't match, trees are not equivalent.
        if not root1 or not root2 or root1.val != root2.val:
            return False

        # Check both the scenarios (with and without flipping)
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or \
               (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))

obj = Solution()
#data = obj.flipEquiv(root1 = [1,2,3,4,5,6,None,None,None,7,8], root2 = [1,3,2,None,6,4,5,None,None,None,None,8,7])
#data = obj.flipEquiv(root1 = [], root2 = [])
data = obj.flipEquiv(root1 = [], root2 = [1])
print(data)