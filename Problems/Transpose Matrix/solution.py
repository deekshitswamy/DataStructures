import io
from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix)
        m=len(matrix[0])
        ans=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j]=matrix[j][i]
        return ans

obj = Solution()
#data = obj.transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]])
data = obj.transpose(matrix = [[1,2,3],[4,5,6]])
print(data)