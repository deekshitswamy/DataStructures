
import io
from math import inf
from typing import List
from functools import cache
from bisect import bisect_left
from collections import defaultdict
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        ### INDEX BUILDING ###
        idxs = defaultdict(list)

        prev_start = -1
        prev = ""
        for i, c in enumerate(s):
            if c != prev:
                idxs[prev].append((prev_start, i-1))
                prev_start = i
                prev = c

        # edge case
        idxs[prev].append((prev_start, i))

        ### MAIN PROGRAM ###
        enc_len = lambda l: 4 if l == 100 \
                       else 3 if l > 9 \
                       else 2 if l > 1 else 1
        @cache
        def dp(i, k, prev_length):
            if k < 0:
                return inf
            
            if i == len(s):
                return 0

            # calculate run length
            pos = bisect_left(idxs[s[i]], (i, i))
            
            j = idxs[s[i]][pos][-1] + 1
            
            length = j - i + prev_length

            # each line below mirrors the five cases 
            # in Intuition section
            ans = min(dp(j, k-length, 0), \
                      1 + dp(j, k-max(length-1, 0), 0), \
                      2 + dp(j, k-max(length-9, 0), 0), \
                      3 + dp(j, k-max(length-99, 0), 0), \
                      enc_len(length) + dp(j, k, 0))
            
            # edge case, e.g., 
            # aabbaa: consider skipping my calculations 
            # and letting next range combine with me
            if pos + 1 < len(idxs[s[i]]):
                l = idxs[s[i]][pos+1][0]
                remove = l - j
                ans = min(ans, dp(l, k - remove, prev_length + j - i))

            return ans
        
        return dp(0, k, 0)

obj = Solution()
#data = obj.getLengthOfOptimalCompression(s = "aaabcccd", k = 2)
#data = obj.getLengthOfOptimalCompression(s = "aabbaa", k = 2)
data = obj.getLengthOfOptimalCompression(s = "aaaaaaaaaaa", k = 0)
print(data)