import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        pass

obj = Solution()
#data = obj.constructFromPrePost(preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1])
data = obj.constructFromPrePost(preorder = [1], postorder = [1])
print(data)