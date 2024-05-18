import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0
        def dfs(root):
            if not root: return 0
            l, r = dfs(root.left), dfs(root.right)
            extraCoins = (root.val - 1) + l + r
            self.moves += abs(extraCoins)
            return extraCoins
        dfs(root)
        return self.moves

obj = Solution()
#data = obj.distributeCoins(root = [3,0,0])
data = obj.distributeCoins(root = [0,3,0])
print(data)