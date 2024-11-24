import io
from typing import List
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        def absSmall(matr):
            small = abs(matr[0][0])
            for i in range(n):
                for j in range(n):
                    small = min(small, abs(matr[i][j]))
            return small
        
        countNegative = 0
        totalSum = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] <0:
                    countNegative +=1
                totalSum += abs(matrix[i][j])
        small = absSmall(matrix)
        if countNegative %2 == 0:
            return totalSum
        else:
            return totalSum - 2*small

obj = Solution()
#data = obj.maxMatrixSum(matrix = [[1,-1],[-1,1]])
data = obj.maxMatrixSum(matrix = [[1,2,3],[-1,-2,-3],[1,2,3]])
print(data)