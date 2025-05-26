import io
from typing import List
from collections import defaultdict
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        N = len(colors)
        dp = [defaultdict(int) for _ in range(N)]

        g = [[] for _ in range(N)]

        for u, v in edges:
            g[u].append(v)

        parents = set()

        visited = set()

        def dfs(s):

            if s in parents:
                return False

            if s in visited:
                return True
            
            parents.add(s)
        
            coldict = defaultdict(int)

            for e in g[s]:
                if not dfs(e):
                    return False

                for col in dp[e]:
                    coldict[col] = max(coldict[col], dp[e][col])
            
            for col in coldict:
                dp[s][col] = coldict[col]
            
            dp[s][colors[s]] += 1
            
            parents.remove(s)

            visited.add(s)

            return True

        for s in range(N):
            if s not in visited and not dfs(s):
                return -1

        return max(max(k.values()) for k in dp)

obj = Solution()
#data = obj.largestPathValue(colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]])
data = obj.largestPathValue(colors = "a", edges = [[0,0]])
print(data)