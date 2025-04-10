import io
from typing import List
from functools import cache
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        @cache
        def dfs(pos: int, lim: int):
            if len(t) < n:
                return 0
            if len(t) - pos == n:
                return int(s <= t[pos:]) if lim else 1
            up = min(int(t[pos]) if lim else 9, limit)
            ans = 0
            for i in range(up + 1):
                ans += dfs(pos + 1, lim and i == int(t[pos]))
            return ans

        n = len(s)
        t = str(start - 1)
        a = dfs(0, True)
        dfs.cache_clear()
        t = str(finish)
        b = dfs(0, True)
        return b - a

obj = Solution()
#data = obj.numberOfPowerfulInt(start = 1, finish = 6000, limit = 4, s = "124")
#data = obj.numberOfPowerfulInt(start = 15, finish = 215, limit = 6, s = "10")
data = obj.numberOfPowerfulInt(start = 1000, finish = 2000, limit = 4, s = "3000")
print(data)