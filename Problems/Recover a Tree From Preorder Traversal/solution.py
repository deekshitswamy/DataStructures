import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        pass

obj = Solution()
#data = obj.recoverFromPreorder(traversal = "1-2--3--4-5--6--7")
#data = obj.recoverFromPreorder(traversal = "1-2--3---4-5--6---7")
data = obj.recoverFromPreorder(traversal = "1-401--349---90--88")
print(data)