import io
from typing import List
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        R = len(grid)
        C = len(grid[0])
        heap = [(grid[0][0],0,0)]
        v = {(0,0)}
        d = defaultdict(int)
        dir = [(-1,0),(0,-1),(1,0),(0,1)]
        temp = 0
        p = [0]
        while heap:
            c,x,y = heapq.heappop(heap)
            temp += 1
            p.append(c)
            for xx,yy in dir:
                if 0<=x+xx<R and 0<=y+yy<C and (xx+x,yy+y) not in v:
                    heapq.heappush(heap,(grid[xx+x][yy+y],xx+x,yy+y))
                    v.add((xx+x,yy+y))
            while heap and heap[0][0] <= c:
                p1,p2,p3 = heapq.heappop(heap)
                temp += 1
                for xx,yy in dir:
                    if 0<=p2+xx<R and 0<=p3+yy<C and (xx+p2,yy+p3) not in v:
                        heapq.heappush(heap,(grid[xx+p2][yy+p3],xx+p2,yy+p3))
                        v.add((xx+p2,yy+p3))
            d[c] = temp

        ans = []
        for q in queries:
            idx = bisect_left(p,q)
            ans.append(d[p[idx-1]])
        return ans

obj = Solution()
#data = obj.maxPoints(grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2])
data = obj.maxPoints(grid = [[5,2,1],[1,1,2]], queries = [3])
print(data)