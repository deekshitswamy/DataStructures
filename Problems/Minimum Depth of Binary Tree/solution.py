import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def count(root):
            if root is None:
                return 0
            if root.left is None:
                return count(root.right) + 1
            if root.right is None:
                return count(root.left) + 1
            return min(count(root.left), count(root.right)) + 1
        return count(root)

# example 1
# node1 = TreeNode(val=7,left=None, right=None)
# node2 = TreeNode(val=15,left=None, right=None)
# node3 = TreeNode(val=9,left=None, right=None)
# node4 = TreeNode(val=20,left=node2, right=node1)
# root = TreeNode(val=3,left=node3, right=node4)

#example 2
node1 = TreeNode(val=6,left=None, right=None)
node2 = TreeNode(val=5,left=None, right=node1)
node3 = TreeNode(val=4,left=None, right=node2)
node4 = TreeNode(val=3,left=None, right=node3)
root = TreeNode(val=2,left=None, right=node4)

obj = Solution()
data = obj.minDepth(root)
print(data)