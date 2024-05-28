import io
from typing import List
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = 0
        current_cost = 0
        max_length = 0

        for end in range(len(s)):
            current_cost += abs(ord(s[end]) - ord(t[end]))

            while current_cost > maxCost:
                current_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1

            max_length = max(max_length, end - start + 1)
        
        return max_length

obj = Solution()
#data = obj.equalSubstring(s = "abcd", t = "bcdf", maxCost = 3)
#data = obj.equalSubstring(s = "abcd", t = "cdef", maxCost = 3)
data = obj.equalSubstring(s = "abcd", t = "acde", maxCost = 0)
print(data)