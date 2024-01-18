import io
from typing import List
class Solution:
    def climbStairs(self, n: int) -> int:
        z = [1, 1, 2]
        for i in range(n - 2):
            z.append(z[-1] + z[-2])
        return z[n]

obj = Solution()
#data = obj.climbStairs(n = 2)
data = obj.climbStairs(n = 2)
print(data)