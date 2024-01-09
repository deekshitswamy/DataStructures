import io
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def check(root,arr):
            if not root:
                return arr
            if not root.left and not root.right:
                arr+=[root.val]
                return arr
            check(root.left,arr)
            check(root.right,arr)
            return arr
        return check(root1,[])==check(root2,[])

obj = Solution()
#data = obj.leafSimilar(n = 1)
#data = obj.leafSimilar(n = 2)
data = obj.leafSimilar(n = 2)
print(data)