import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root:
            root.left=self.removeLeafNodes(root.left,target)
            root.right=self.removeLeafNodes(root.right,target)
            if root.val==target and not root.left and not root.right:
                root=None

        return root

obj = Solution()
#data = obj.removeLeafNodes(root = [1,2,3,2,null,2,4], target = 2)
#data = obj.removeLeafNodes(root = [1,3,3,3,2], target = 3)
data = obj.removeLeafNodes(root = [1,2,None,2,None,2], target = 2)
print(data)