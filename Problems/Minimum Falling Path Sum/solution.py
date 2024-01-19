import io
from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        for r in range(n):
            for c in range(m):
                if r>0 and 0<=c-1 and c+1<m:
                    matrix[r][c]=min(matrix[r][c]+matrix[r-1][c],matrix[r][c]+matrix[r-1][c+1],matrix[r][c]+matrix[r-1][c-1])
                elif r>0 and c-1==-1:
                    matrix[r][c]=min(matrix[r][c]+matrix[r-1][c],matrix[r][c]+matrix[r-1][c+1])
                elif r>0 and c+1==m:
                    matrix[r][c]=min(matrix[r][c]+matrix[r-1][c],matrix[r][c]+matrix[r-1][c-1])

        return min(matrix[n-1])

obj = Solution()
#data = obj.minFallingPathSum(matrix = [[2,1,3],[6,5,4],[7,8,9]])
data = obj.minFallingPathSum(matrix = [[-19,57],[-40,-5]])
print(data)