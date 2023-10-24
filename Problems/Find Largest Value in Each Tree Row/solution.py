import io
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: List[int]) -> List[int]:
        if not root: return []
        a, depth = {}, 0
        stack = [(root, depth)]
        while stack:
            node, depth = stack.pop()
            if depth in a and a[depth] < node.val: a[depth] = node.val
            if depth not in a: a[depth] = node.val
            if node.left: stack.append((node.left, 1 + depth))
            if node.right: stack.append((node.right, 1 + depth))
        return a.values()

obj = Solution()
#data = obj.largestValues(root = [1,3,2,5,3,null,9])
data = obj.largestValues(root = [1,2,3])
print(data)