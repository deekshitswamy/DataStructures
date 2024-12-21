import io
from typing import List
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = defaultdict(list)
        src = 0
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        comp = 0
        visited = set()
        def dfs(root):
            nonlocal comp
            if root in visited:
                return 0
            visited.add(root)
            ans = values[root]
            for neigh in adj[root]:
                ans += dfs(neigh)
            if ans % k == 0:
                comp += 1
                return 0
            return ans % k
        dfs(src)
        return comp

obj = Solution()
#data = obj.maxKDivisibleComponents(n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6)
data = obj.maxKDivisibleComponents(n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3)
print(data)