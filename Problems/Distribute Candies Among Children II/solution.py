import io
from typing import List
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def comb2(k):
            return k * (k - 1) // 2 if k >= 2 else 0

        def f(s):
            return comb2(s + 2)

        a = f(n)
        b = f(n - (limit + 1))
        c = f(n - 2 * (limit + 1))
        d = f(n - 3 * (limit + 1))
        return a - 3 * b + 3 * c - d

obj = Solution()
#data = obj.distributeCandies(n = 5, limit = 2)
data = obj.distributeCandies(n = 3, limit = 3)
print(data)