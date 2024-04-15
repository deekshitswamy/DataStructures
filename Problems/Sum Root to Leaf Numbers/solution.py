import io
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(cur,num):
            if not cur:return 0
            
            num=num*10+cur.val
            
            if not cur.left and not cur.right:
                return num
            
            return dfs(cur.left,num)+dfs(cur.right,num)
        
        return dfs(root,0)

obj = Solution()
#data = obj.sumNumbers(root = [1,2,3])
data = obj.sumNumbers(root = [4,9,0,5,1])
print(data)