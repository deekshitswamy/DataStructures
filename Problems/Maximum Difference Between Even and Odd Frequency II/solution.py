import io
from math import inf
from typing import List
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        prefix = [[0] * (n + 1) for _ in range(5)]
        for i, ch in enumerate(s):
            d = ord(ch) - 48
            for j in range(5):
                prefix[j][i + 1] = prefix[j][i]
            prefix[d][i + 1] += 1
        ans = -inf
        for ia in range(5):
            for ib in range(5):
                if ia == ib:
                    continue
                min_diff = [inf] * 4
                l = 0
                for r in range(n):
                    pa = prefix[ia][r + 1]
                    pb = prefix[ib][r + 1]
                    while r - l + 1 >= k and prefix[ia][l] < pa and prefix[ib][l] < pb:
                        pa_l = prefix[ia][l]
                        pb_l = prefix[ib][l]
                        idx_l = (pa_l % 2) * 2 + (pb_l % 2)
                        min_diff[idx_l] = min(min_diff[idx_l], pa_l - pb_l)
                        l += 1
                    idx = (1 - pa % 2) * 2 + (pb % 2)
                    ans = max(ans, pa - pb - min_diff[idx])
        return ans

obj = Solution()
#data = obj.maxDifference(s = "12233", k = 4)
#data = obj.maxDifference(s = "1122211", k = 3)
data = obj.maxDifference(s = "110", k = 3)
print(data)