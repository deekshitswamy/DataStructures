import io
from typing import List
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        limits = {c: s.count(c) - k for c in 'abc'}
        if any(x < 0 for x in limits.values()):
            return -1

        cnts = {c: 0 for c in 'abc'}
        ans = l = 0
        for r, c in enumerate(s):
            cnts[c] += 1
            while cnts[c] > limits[c]:
                cnts[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return len(s) - ans

obj = Solution()
#data = obj.takeCharacters(s = "aabaaaacaabc", k = 2)
data = obj.takeCharacters(s = "a", k = 1)
print(data)