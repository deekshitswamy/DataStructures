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
    def minimumOperations(self, root: TreeNode) -> int:
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        def f(t):
            n = len(t)
            m = {v: i for i, v in enumerate(sorted(t))}
            for i in range(n):
                t[i] = m[t[i]]
            ans = 0
            for i in range(n):
                while t[i] != i:
                    swap(t, i, t[i])
                    ans += 1
            return ans

        q = deque([root])
        ans = 0
        while q:
            t = []
            for _ in range(len(q)):
                node = q.popleft()
                t.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans += f(t)
        return ans

obj = Solution()
#data = obj.minimumOperations(root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10])
#data = obj.minimumOperations(root = [1,3,2,7,6,5,4])
data = obj.minimumOperations(root = [1,2,3,4,5,6])
print(data)