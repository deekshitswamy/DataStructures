import io
from typing import List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q=deque([root])
        while q:
            node=q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return node.val 

obj = Solution()
#data = obj.findBottomLeftValue(root = [2,1,3])
data = obj.findBottomLeftValue(root = [1,2,3,4,None,5,6,None,None,7])
print(data)