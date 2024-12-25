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
        answer = {}
        
        def dfs(root, level):
            if root:
                # Update the maximum value for the current level
                if level in answer:
                    answer[level] = max(answer[level], root.val)
                else:
                    answer[level] = root.val
                # Traverse the left and right children
                dfs(root.left, level + 1)
                dfs(root.right, level + 1)
        
        dfs(root, 0)
        # Return the values in the order they were filled
        return list(answer.values())

obj = Solution()
#data = obj.largestValues(root = [1,3,2,5,3,null,9])
data = obj.largestValues(root = [1,2,3])
print(data)