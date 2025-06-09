import io
from typing import List
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(curr, n):
            steps = 0
            first = curr
            next_prefix = curr + 1
            while first <= n:
                steps += min(n + 1, next_prefix) - first
                first *= 10
                next_prefix *= 10
            return steps
        
        curr = 1
        k -= 1
        
        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                k -= steps
                curr += 1
            else:
                curr *= 10
                k -= 1
        
        return curr

obj = Solution()
#data = obj.findKthNumber(n = 13, k = 2)
data = obj.findKthNumber(n = 1, k = 1)
print(data)