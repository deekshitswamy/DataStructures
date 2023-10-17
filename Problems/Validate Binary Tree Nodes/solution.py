import io
from typing import List
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        pass


obj = Solution()
#data = obj.validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1])
#data = obj.validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1])
data = obj.validateBinaryTreeNodes(n = 2, leftChild = [1,0], rightChild = [-1,-1])
print(data)