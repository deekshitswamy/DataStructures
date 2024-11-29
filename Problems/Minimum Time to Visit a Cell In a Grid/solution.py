import io
from typing import List
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        if min(grid[0][1], grid[1][0]) > 1:
            return -1

        pq = []
        heappush(pq, (0, 0, 0))

        visited = [[False] * col for _ in range(row)]
        visited[0][0] = True

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while pq:
            time, x, y = heappop(pq)

            if x == row - 1 and y == col - 1:
                return time

            for dx, dy in directions:
                newX, newY = x + dx, y + dy

                if 0 <= newX < row and 0 <= newY < col and not visited[newX][newY]:
                    diff = abs(grid[newX][newY] - time)
                    waitingTime = 1 if diff % 2 == 0 else 0
                    newTime = max(grid[newX][newY] + waitingTime, time + 1)
                    heappush(pq, (newTime, newX, newY))
                    visited[newX][newY] = True

        return -1

obj = Solution()
#data = obj.minimumTime(grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]])
data = obj.minimumTime(grid = [[0,2,4],[3,2,1],[1,0,4]])
print(data)