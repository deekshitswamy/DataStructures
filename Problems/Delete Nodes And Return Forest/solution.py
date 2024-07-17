import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        result = []
        def dfs(parent: TreeNode, node: TreeNode):
            nonlocal result
            if not node:
                return
            if node.val in to_delete:
                if parent:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                dfs(None, node.left)
                dfs(None, node.right)
            else:
                if not parent:
                    result.append(node)
                dfs(node, node.left)
                dfs(node, node.right)
        dfs(None, root)
        return result

obj = Solution()
#data = obj.delNodes(root = [1,2,3,4,5,6,7], to_delete = [3,5])
data = obj.delNodes(root = [1,2,4,None,3], to_delete = [3])
print(data)