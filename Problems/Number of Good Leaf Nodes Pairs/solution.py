import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0
        def dfs(root):
            if not root: return []
            if not root.left and not root.right: return [1]
            left = dfs(root.left)
            right = dfs(root.right)
            for i in left:
                for j in right:
                    if i+j <= distance:
                        self.ans += 1
            return [i+1 for i in left+right if i+1 < distance]
        dfs(root)
        return self.ans

obj = Solution()
#data = obj.countPairs(root = [1,2,3,None,4], distance = 3)
#data = obj.countPairs(root = [1,2,3,4,5,6,7], distance = 3)
data = obj.countPairs(root = [7,1,4,6,None,5,3,None,None,None,None,None,2], distance = 3)
print(data)