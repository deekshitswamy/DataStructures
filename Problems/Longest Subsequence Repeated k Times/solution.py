import io
from typing import List
from collections import Counter
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        c = Counter(s)
        chars = options = {char for char, v in c.items() if v >= k}
        if not options:
            return ''
        def check(sub):
            sub_it = iter(sub * k)
            it = iter(s)
            return all(c in it for c in sub_it)
        for _ in range(len(s) // k - 1):
            new = set()
            for op in options:
                for char in chars:
                    if op[1:] + char in options and check(op + char):
                        new.add(op + char)
            if not new:
                return max(options)
            options = new
        return max(options)

obj = Solution()
#data = obj.longestSubsequenceRepeatedK(s = "letsleetcode", k = 2)
#data = obj.longestSubsequenceRepeatedK(s = "bb", k = 2)
data = obj.longestSubsequenceRepeatedK(s = "ab", k = 2)
print(data)