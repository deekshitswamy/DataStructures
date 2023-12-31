import io
from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        l= 0

        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                time += min(neededTime[l] , neededTime[r])
                if neededTime[l] < neededTime[r]:
                    l = r
            else:
                l = r
        return time

obj = Solution()
#data = obj.minCost(colors = "abaac", neededTime = [1,2,3,4,5])
#data = obj.minCost(colors = "abc", neededTime = [1,2,3])
data = obj.minCost(colors = "aabaa", neededTime = [1,2,3,4,1])
print(data)