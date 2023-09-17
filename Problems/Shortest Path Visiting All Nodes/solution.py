import io
from collections import deque
from typing import List
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n=len(graph)
        queue=deque([(i,1<<i) for i in range(n)])
        seen=set(queue)
        ans=0
        while queue:
            for _ in range(len(queue)):
                u,m=queue.popleft()
                if m==(1<<n)-1:
                    return ans
                for v in graph[u]:
                    if (v,m|1<<v) not in seen:
                        queue.append((v,m|1<<v))
                        seen.add((v,m|1<<v))
            ans+=1                

obj = Solution()
#data = obj.shortestPathLength(graph = [[1,2,3],[0],[0],[0]])
data = obj.shortestPathLength(graph = [[1],[0,2,4],[1,3,4],[2],[1,2]])
print(data)