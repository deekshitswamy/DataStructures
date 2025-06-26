import io
from typing import List
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        cnt0 = s.count("0")
        n = len(s)
        j = n - 1
        a = ""
        cnta0 = 0
        
        while j >= 0:
            candidate = a + s[j]
            if int(candidate[::-1], 2) <= k:
                a += s[j]
                if s[j] == "0":
                    cnta0 += 1
            else:
                break
            j -= 1
        
        return len(a) + (cnt0 - cnta0)

obj = Solution()
#data = obj.longestSubsequence(s = "1001010", k = 5)
data = obj.longestSubsequence(s = "00101001", k = 1)
print(data)