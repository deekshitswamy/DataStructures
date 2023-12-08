import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root:TreeNode) -> str:
        ans=[]
        def preorder(root):
            if not root:
                return
            ans.append("(")
            ans.append(str(root.val))
            if not root.left and root.right:
                ans.append("()")
            preorder(root.left)
            preorder(root.right)
            ans.append(")")
        preorder(root)            
        return "".join(ans)[1:-1]

obj = Solution()
#data = obj.tree2str(root = [1,2,3,4])
data = obj.tree2str(root = [1,2,3,None,4])
print(data)