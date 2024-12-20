import io
from typing import List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: TreeNode) -> TreeNode:
        queue = deque()
        level = 0
        queue.append(root)

        while queue:
            size = len(queue)
            if level % 2 != 0:
                nodes_at_level = []

                for _ in range(size):
                    node = queue.popleft()
                    nodes_at_level.append(node)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                # Reverse the values at the current odd level
                n = len(nodes_at_level)
                for i in range(n // 2):
                    nodes_at_level[i].val, nodes_at_level[n - i - 1].val = (
                        nodes_at_level[n - i - 1].val, nodes_at_level[i].val
                    )

            else:
                for _ in range(size):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            level += 1

        return root

obj = Solution()
#data = obj.reverseOddLevels(root = [2,3,5,8,13,21,34])
#data = obj.reverseOddLevels(root = [7,13,11])
data = obj.reverseOddLevels(root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2])
print(data)