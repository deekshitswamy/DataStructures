import io
from typing import List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        D = defaultdict(int)

        def dfs(tree):

            if not tree:
                return

            else:
                D[tree.val] += 1
                dfs(tree.left)
                dfs(tree.right)

        dfs(root)

        M = max(list(D.values()))
        return [x for x in list(D.keys()) if D[x] == M]

obj = Solution()
#data = obj.findMode(root = [1,null,2,2])
data = obj.findMode(root = [0])
print(data)