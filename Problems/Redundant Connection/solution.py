import io
from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        src = [n for n in range(len(edges) + 1)] 

        def find(x):
            src[x] = x if src[x] == x else find(src[x])
            return src[x]
        
        for a, b in edges:
            src_a, src_b = find(a), find(b)
            if src_a == src_b:
                return [a,b] 
                              
            src[src_b] = src_a

obj = Solution()
#data = obj.findRedundantConnection(edges = [[1,2],[1,3],[2,3]])
data = obj.findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]])
print(data)