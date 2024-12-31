import io
from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        a, b, c = costs
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i >= len(days):
                return 0

            res = float("inf")
            for cost, duration in [(a,1),(b,7),(c,30)]:
                j = i
                while j < len(days) and days[i] + duration - 1 >= days[j]:
                    j += 1
                res = min(res, cost + dfs(j))
            dp[i] = res

            return dp[i]
        return dfs(0)

obj = Solution()
#data = obj.mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15])
data = obj.mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15])
print(data)