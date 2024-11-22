import io
from typing import List
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_count = defaultdict(int)
        
        for row in matrix:
            pattern = ''.join('1' if (row[i] ^ row[0]) else '0' for i in range(len(row)))
            pattern_count[pattern] += 1
        
        return max(pattern_count.values())

obj = Solution()
#data = obj.maxEqualRowsAfterFlips(matrix = [[0,1],[1,1]])
#data = obj.maxEqualRowsAfterFlips(matrix = [[0,1],[1,0]])
data = obj.maxEqualRowsAfterFlips(matrix = [[0,0,0],[0,0,1],[1,1,0]])
print(data)