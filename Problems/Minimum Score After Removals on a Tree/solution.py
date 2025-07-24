import io
from typing import List
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        ans = float('inf')
        def dfs(v, visited, subs):
            ret = nums[v]
            for u in graph[v]:
                if u not in visited:
                    visited.add(u)
                    cur = dfs(u, visited, subs)
                    ret ^= cur
                    subs.add(cur)
            return ret
        for u, v in edges:
            graph[u].remove(v)
            graph[v].remove(u)
            leftsubs, rightsubs = set(), set()
            left, right = dfs(u, {u}, leftsubs), dfs(v, {v}, rightsubs)
            for c in leftsubs:
                parts = [right, c, left ^ c]
                ans = min(ans, max(parts) - min(parts))
            for c in rightsubs:
                parts = [left, c, right ^ c]
                ans = min(ans, max(parts) - min(parts))
            graph[u].add(v)
            graph[v].add(u)
        return ans

obj = Solution()
#data = obj.minimumScore(nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]])
data = obj.minimumScore(nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]])
print(data)