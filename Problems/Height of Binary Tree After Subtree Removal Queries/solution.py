import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root: TreeNode, queries: List[int]) -> List[int]:
        pass

obj = Solution()
#data = obj.treeQueries(root = [1,3,4,2,None,6,5,None,None,None,None,None,7], queries = [4])
data = obj.treeQueries(root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8])
print(data)