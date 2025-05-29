import io
from typing import List
from collections import deque
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        g1 = defaultdict(list)
        g2 = defaultdict(list)
        n = len(edges1)
        m = len(edges2)
        def buildGraph(edges,g):
            for s, e in edges:
                g[s].append(e)
                g[e].append(s)
        
        buildGraph(edges1, g1)
        buildGraph(edges2, g2)
        
        g1_target = [0 for i in range(n+1)]
        g1_odd_even_arr = [False for i in range(n+1)]
        g2_target = [0 for i in range(m+1)]
        g2_odd_even_arr = [False for i in range(m+1)]

        def dfs(source, odd_even_arr, g):
            seen = set()
            odd = 0
            even = 0
            def odd_even(source, cur):
                nonlocal odd, even
                if source in seen:
                    return 
                if cur%2==0:
                    even+=1
                    odd_even_arr[source] = True
                else:
                    odd+=1
                    odd_even_arr[source] = False
                seen.add(source)
                for nbr in g[source]:
                    odd_even(nbr, cur+1)
            odd_even(0, 0)
            return odd, even

        g1_odd, g1_even = dfs(0, g1_odd_even_arr, g1)
        g2_odd, g2_even = dfs(0, g2_odd_even_arr, g2)
        for i in range(n+1):
            if g1_odd_even_arr[i]:
                g1_target[i] = g1_even
            else:
                g1_target[i] = g1_odd

        res = []
        for i in range(n+1):
            res.append(g1_target[i]+max(g2_even, g2_odd))
        return res

obj = Solution()
#data = obj.maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]])
data = obj.maxTargetNodes(edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]])
print(data)