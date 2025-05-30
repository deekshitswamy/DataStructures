import io
from typing import List
from collections import deque
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        inf = 1e9 + 7
        dist1 = [inf] * n
        dist2 = [inf] * n

        def bfs(start: int, dist: List[int]):
            visited = set()
            q = deque([(start, 0)])
            while q:
                node, d = q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                dist[node] = d
                nbr = edges[node]
                if nbr != -1:
                    q.append((nbr, d + 1))

        bfs(node1, dist1)
        bfs(node2, dist2)

        resIndex = -1
        miniDistance = inf

        for i in range(n):
            if dist1[i] != inf and dist2[i] != inf:
                maxDist = max(dist1[i], dist2[i])
                if resIndex == -1 or maxDist < miniDistance:
                    miniDistance = maxDist
                    resIndex = i

        return resIndex

obj = Solution()
#data = obj.closestMeetingNode(edges = [2,2,3,-1], node1 = 0, node2 = 1)
data = obj.closestMeetingNode(edges = [1,2,-1], node1 = 0, node2 = 2)
print(data)