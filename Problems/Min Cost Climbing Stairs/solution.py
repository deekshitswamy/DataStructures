import io
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        prev2=cost[0]
        prev1=cost[1]
        for i in range(2,n):
            temp=cost[i]+min(prev1,prev2)
            prev2=prev1
            prev1=temp
        return min(prev1,prev2)

obj = Solution()
#data = obj.minCostClimbingStairs(cost = [10,15,20])
data = obj.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1])
print(data)