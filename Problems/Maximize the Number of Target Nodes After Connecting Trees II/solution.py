import io
from typing import List
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def parity(edges, n):
            g = [[] for _ in range(n)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
            q, even = deque([(0, -1, 1)]), [0] * n
            while q:
                u, p, e = q.popleft()
                even[u] = e
                for v in g[u]:
                    if v != p: q.append((v, u, 1 - e))
            return even

        n1, n2 = len(e1)+1, len(e2)+1
        p1, p2 = parity(e1, n1), parity(e2, n2)
        s1, s2 = sum(p1), sum(p2)
        mx = max(s2, n2 - s2)
        return [mx + (s1 if x else n1 - s1) for x in p1]

obj = Solution()
#data = obj.maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]])
data = obj.maxTargetNodes(edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]])
print(data)