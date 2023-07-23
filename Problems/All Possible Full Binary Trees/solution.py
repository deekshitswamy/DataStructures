import io
from typing import List
from collections import defaultdict
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        memo = {1: [TreeNode(0)]}
        def f(n: int) -> List[TreeNode]:

            if n == 1:
                return [TreeNode(0)]
            if n % 2 == 0:
                return []

            ans: List[TreeNode] = []
            left_num: int = 1
            right_num: int = n - 2

            while right_num > 0:
                left: List[TreeNode] = f(left_num) if left_num not in memo else memo[left_num]
                right: List[TreeNode] = f(right_num) if right_num not in memo else memo[right_num]

                for i in range(len(left)):
                    for j in range(len(right)):
                        root: TreeNode = TreeNode(0)
                        root.left = left[i]
                        root.right = right[j]
                        ans.append(root)

                left_num += 2
                right_num -= 2

            memo[n] = ans

            return ans
 
        return f(n)

# example 1
#n = 7
root = TreeNode()

#example 2
#n = 3
root = TreeNode()

obj = Solution()
data = obj.allPossibleFBT(root)
print(data)