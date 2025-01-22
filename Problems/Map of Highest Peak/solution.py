import io
import collections
from typing import List
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows=len(isWater)
        cols=len(isWater[0])
        inf=10**9
        dist=[[inf]*cols for _ in range(rows)]
        q=collections.deque()
        for x in range(rows):
            for y in range(cols):
                if isWater[x][y]==1:
                    dist[x][y]=0
                    q.append((0,x,y))
                    
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        while len(q)>0:
            d,x,y=q.popleft()
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<rows and 0<=ny<cols and dist[nx][ny]==inf:
                    dist[nx][ny]=d+1
                    q.append((d+1,nx,ny))
        return dist

obj = Solution()
#data = obj.highestPeak(isWater = [[0,1],[0,0]])
data = obj.highestPeak(isWater = [[0,0,1],[1,0,0],[0,0,0]])
print(data)