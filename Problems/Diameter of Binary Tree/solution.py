import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans=0
        def depth(node):
            if not node:
                return 0
            left_depth=depth(node.left)
            right_depth=depth(node.right)
            self.ans=max(self.ans,left_depth+right_depth)
            return max(left_depth,right_depth)+1
        depth(root)
        return self.ans

obj = Solution()
#data = obj.diameterOfBinaryTree(root = [1,2,3,4,5])
data = obj.diameterOfBinaryTree(root = [1,2])
print(data)