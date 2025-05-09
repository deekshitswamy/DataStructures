import io
from math import comb
from typing import List
from functools import lru_cache
from collections import Counter
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        velunexorai = num  # Store input as per instruction
        digit_counts = Counter(int(ch) for ch in velunexorai)
        total_sum = sum(int(ch) for ch in velunexorai)

        if total_sum % 2 != 0:
            return 0  # Can't split into two equal halves

        half_sum = total_sum // 2
        n = len(velunexorai)
        odd_count = n // 2
        even_count = n - odd_count

        @lru_cache(None)
        def dfs(d, odd_remain, even_remain, balance):
            if odd_remain == 0 and even_remain == 0 and balance == 0:
                return 1
            if d < 0 or odd_remain < 0 or even_remain < 0 or balance < 0:
                return 0

            res = 0
            total_available = digit_counts[d]

            # Try using j copies of digit d in the odd positions
            for odd_used in range(total_available + 1):
                even_used = total_available - odd_used
                if odd_used > odd_remain or even_used > even_remain:
                    continue

                ways_odd = comb(odd_remain, odd_used)
                ways_even = comb(even_remain, even_used)
                sub_res = dfs(
                    d - 1,
                    odd_remain - odd_used,
                    even_remain - even_used,
                    balance - d * odd_used
                )
                res = (res + ways_odd * ways_even * sub_res) % MOD

            return res

        return dfs(9, odd_count, even_count, half_sum)

obj = Solution()
#data = obj.countBalancedPermutations(num = "123")
#data = obj.countBalancedPermutations(num = "112")
data = obj.countBalancedPermutations(num = "12345")
print(data)