import io
from typing import List
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def isPossible(x: int, quantities: list[int], n: int) -> bool:
            sum = 0
            for u in quantities:
                sum += -(-u // x)  # Equivalent to ceil(u / x)
            return sum > n

        left, right = 1, 100000
        while left < right:
            mid = (left + right) // 2
            if isPossible(mid, quantities, n):
                left = mid + 1
            else:
                right = mid
        return left

obj = Solution()
#data = obj.minimizedMaximum(n = 6, quantities = [11,6])
#data = obj.minimizedMaximum(n = 7, quantities = [15,10,10])
data = obj.minimizedMaximum(n = 1, quantities = [100000])
print(data)