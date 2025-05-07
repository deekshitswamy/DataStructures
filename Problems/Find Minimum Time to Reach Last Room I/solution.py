import io
from typing import List
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])
        moves = [(0, 0, 0)]
        visits = set()
        minima = 0
        while moves:
            tym, row, col = heapq.heappop(moves)
            if row == rows - 1 and col == cols - 1: 
                minima = tym
                break
            for rx, cx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                rowx, colx = row + rx, col + cx
                if not 0 <= rowx < rows or not 0 <= colx < cols: 
                    continue
                if (rowx, colx) in visits: 
                    continue
                reach = max(tym, moveTime[rowx][colx]) + 1
                visits.add((rowx,colx))
                heapq.heappush(moves, (reach, rowx, colx))
        return minima

obj = Solution()
#data = obj.minTimeToReach(moveTime = [[0,4],[4,4]])
#data = obj.minTimeToReach(moveTime = [[0,0,0],[0,0,0]])
data = obj.minTimeToReach(moveTime = [[0,1],[1,2]])
print(data)