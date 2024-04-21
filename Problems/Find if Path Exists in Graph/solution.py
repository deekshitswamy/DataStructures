import io
from typing import List
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=set()

        def dfs(root):
            if root==destination:
                return True
            else:
                visited.add(root)
                for i in adj[root]:
                    if i not in visited and dfs(i):
                        return True 
                return False
        return dfs(source)

obj = Solution()
#data = obj.validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2)
data = obj.validPath(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5)
print(data)