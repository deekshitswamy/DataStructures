import io
from typing import List
from collections import deque
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m,n=len(grid), len(grid[0])
        dir=[(0,1),(1,0),(-1,0),(0,-1)]

        q=deque([(0,0,0)])
        visit=[[False] *n for i in range(m)]
        visit[0][0]=True
        while q:
            x,y,cost=q.popleft()

            if x==m-1 and y==n-1:
                return cost
            for dx,dy in dir:
                newx,newy=x+dx,y+dy

                if 0<=newx <m and 0<=newy<n and not visit[newx][newy]:
                    visit[newx][newy]=True
                    if grid[newx][newy]==1:
                        q.append((newx,newy,cost+1))
                    else:
                        q.appendleft((newx,newy,cost))
        return 0

obj = Solution()
#data = obj.minimumObstacles(grid = [[0,1,1],[1,1,0],[1,1,0]])
data = obj.minimumObstacles(grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]])
print(data)