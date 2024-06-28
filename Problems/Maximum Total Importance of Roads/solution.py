import io
from typing import List
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees=[0]*n
        for u,v in roads:
            degrees[u]+=1
            degrees[v]+=1
        degrees.sort()
        degrees.reverse()  
        ans=0
        for i,j in enumerate(degrees):
            ans+=(n-i)*j
        return ans

obj = Solution()
#data = obj.maximumImportance(n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]])
data = obj.maximumImportance(n = 5, roads = [[0,3],[2,4],[1,3]])
print(data)