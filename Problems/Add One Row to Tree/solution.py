import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth ==1:
            r = root
            root = TreeNode(val,left=r)
            return root
            
        q = [(root,1)]
        while q:
            node,cur_depth = q.pop(0)
            if cur_depth == depth-1:
                left = node.left
                right=node.right
                node.left = TreeNode(val,left=left)
                node.right = TreeNode(val,right=right)
            else:
                if node.left:
                    q.append((node.left,cur_depth+1))
                if node.right:
                    q.append((node.right,cur_depth+1))
        return root

obj = Solution()
#data = obj.addOneRow(root = [4,2,6,3,1,5], val = 1, depth = 2)
data = obj.addOneRow(root = [4,2,None,3,1], val = 1, depth = 3)
print(data)