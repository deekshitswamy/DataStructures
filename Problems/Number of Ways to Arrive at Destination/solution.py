import io
from typing import List
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        modulo = 1_000_000_007

        vs = defaultdict(dict)
        for u, v, time in roads:
            vs[u][v] = time
            vs[v][u] = time
        
        h = [(0, 0)]  # dist, number

        inf = float('inf')
        dist = {
            i: [inf, 0]  # dist, cnt
            for i in range(n)
        }
        dist[0] = [0, 1]

        result = 0
        while h:
            d, u = heapq.heappop(h)
            if d > dist[u][0]:
                continue
            
            for v, time in vs[u].items():
                if d + time == dist[v][0]:
                    dist[v][1] = (dist[v][1] + dist[u][1]) % modulo
                elif d + time < dist[v][0]:
                    dist[v][0] = d + time
                    dist[v][1] = dist[u][1]
                    heapq.heappush(h, [d + time, v])

        return dist[n - 1][1]

obj = Solution()
#data = obj.countPaths(n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]])
data = obj.countPaths(n = 2, roads = [[1,0,10]])
print(data)