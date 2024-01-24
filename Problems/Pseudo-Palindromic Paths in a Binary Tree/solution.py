import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        pass

obj = Solution()
#data = obj.pseudoPalindromicPaths(root = [2,3,1,3,1,null,1])
#data = obj.pseudoPalindromicPaths(root = [2,1,1,1,3,null,null,null,null,null,1])
data = obj.pseudoPalindromicPaths(root = [9])
print(data)