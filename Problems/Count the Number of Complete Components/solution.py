import io
from typing import List
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        X = [[] for i in range(n)]
        for u, v in edges:
            X[u].append(v)
            X[v].append(u)

        visited = [0] * n
        res = 0
        for i in range(n):
            if visited[i]:
                continue
            bfs = [i]
            visited[i] = 1
            for j in bfs:
                for k in X[j]:
                    if visited[k] == 0:
                        bfs.append(k)
                        visited[k] = 1
            if all(len(X[j]) == len(bfs) - 1 for j in bfs):
                res += 1
        return res

obj = Solution()
#data = obj.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4]])
data = obj.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]])
print(data)