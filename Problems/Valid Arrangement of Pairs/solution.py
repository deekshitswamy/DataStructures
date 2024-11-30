import io
from typing import List
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        d = defaultdict(int)
        for u, v in pairs:
            g[u].append(v)
            d[u] += 1
            d[v] -= 1
        
        s = pairs[0][0]
        for u in d:
            if d[u] == 1: s = u
        
        ans = []
        def dfs(u: int) -> None:
            while g[u]:
                v = g[u].pop()
                dfs(v)
                ans.append([u, v])
    
        dfs(s)
        return ans[::-1]

obj = Solution()
#data = obj.validArrangement(pairs = [[5,1],[4,5],[11,9],[9,4]])
#data = obj.validArrangement(pairs = [[1,3],[3,2],[2,1]])
data = obj.validArrangement(pairs = [[1,2],[1,3],[2,1]])
print(data)