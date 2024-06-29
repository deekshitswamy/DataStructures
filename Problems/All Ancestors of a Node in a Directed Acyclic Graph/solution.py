import io
from typing import List
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph=[[] for _ in range(n)]
        indegrees=[0]*n
        for edge in edges:
            src=edge[0]
            dest=edge[1]
            graph[src].append(dest)
            indegrees[dest]+=1
        queue=deque()
        ans=[set() for _ in range(n)]
        for i in range(len(indegrees)):
            if indegrees[i]==0:
                queue.append(i)
        while queue:
            cur=queue.pop()
            for neig in graph[cur]:
                ans[neig].add(cur)
                ans[neig].update(ans[cur])
                indegrees[neig]-=1
                if indegrees[neig]==0:
                    queue.append(neig)
        ans=[(sorted(list(s))) for s in ans]
        return ans

obj = Solution()
#data = obj.getAncestors(n = 8, edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]])
data = obj.getAncestors(n = 5, edgeList = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])
print(data)