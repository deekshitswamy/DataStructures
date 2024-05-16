import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: TreeNode) -> bool:
        def go(node):
            if node is None:
                return True
            if node.left is None and node.right is None:
                if node.val==0:
                    return False
                else:
                    return True
            if node.val==2:
                return go(node.left)  or go(node.right)
            else:
                return go(node.left) and go(node.right)
        return go(root) 

obj = Solution()
#data = obj.evaluateTree(root = [2,1,3,null,null,0,1])
data = obj.evaluateTree(root = [0])
print(data)