import io
import heapq
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        max_heap = []
    
        def dfs(childArr):
            if not childArr:
                return
            sum_val = 0
            nextChildArr = []
            for child in childArr:
                sum_val += child.val
                if child.left:
                    nextChildArr.append(child.left)
                if child.right:
                    nextChildArr.append(child.right)
            heapq.heappush(max_heap, -sum_val)  # Using a min-heap with negative values to simulate max-heap
            dfs(nextChildArr)
        
        dfs([root])
        
        top = -1
        while k:
            top = -heapq.heappop(max_heap)
            k -= 1
            
        return top if top != -1 else -1

obj = Solution()
#data = obj.kthLargestLevelSum(root = [5,8,9,2,1,3,7,4,6], k = 2)
data = obj.kthLargestLevelSum(root = [1,2,None,3], k = 1)
print(data)