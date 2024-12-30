import io
from typing import List
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        memo = {}

        def rec(length):
            if length > high:
                return 0
            
            if length in memo:
                return memo[length]
            
            count = 1 if low <= length <= high else 0

            count += rec(length + zero) % MOD
            count += rec(length + one) % MOD
            count %= MOD
            
            memo[length] = count
            return count

        return rec(0)

obj = Solution()
#data = obj.countGoodStrings(low = 3, high = 3, zero = 1, one = 1)
data = obj.countGoodStrings(low = 2, high = 3, zero = 1, one = 2)
print(data)