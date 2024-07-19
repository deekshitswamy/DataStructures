import io
from typing import List
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mn=[min(i) for i in matrix]
        mx,ans=[],[]
        for i in range(len(matrix[0])):mx.append(max(matrix[j][i] for j in range(len(matrix))))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==mn[i]==mx[j]:ans.append(matrix[i][j])
        return ans

obj = Solution()
#data = obj.luckyNumbers(matrix = [[3,7,8],[9,11,13],[15,16,17]])
#data = obj.luckyNumbers(matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]])
data = obj.luckyNumbers(matrix = [[7,8],[1,2]])
print(data)