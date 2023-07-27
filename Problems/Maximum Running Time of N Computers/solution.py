import io
from typing import List
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        total_runtime = sum(batteries)
        max_runtime = total_runtime // n
        
        for battery in reversed(batteries):
            if battery <= max_runtime:
                break
            total_runtime -= battery
            n -= 1
            max_runtime = total_runtime // n
            
        return max_runtime

obj = Solution()
#data = obj.maxRunTime(n = 2, batteries = [3,3,3])
data = obj.maxRunTime(n = 2, batteries = [1,1,1,1])
print(data)