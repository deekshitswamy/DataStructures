import io
from typing import List
class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = del_a_count = i = res = 0
        while i < len(s):
            if s[i] == 'b':
                b_count += 1
                if i + 1 < len(s) and s[i+1] == 'a':
                    a_count = 0
                    j = i + 1
                    while j < len(s) and s[j] == 'a':
                        a_count += 1
                        j += 1
                    if a_count < b_count - del_a_count:
                        res += a_count
                        del_a_count += a_count
                    else:
                        res += b_count
                        res -= del_a_count # correct the internal a's
                        b_count = del_a_count = 0
                    i = j  # can directly jump to j
                else:
                    i += 1
            else:
                i += 1
        
        return res

obj = Solution()
#data = obj.minimumDeletions(s = "aababbab")
data = obj.minimumDeletions(s = "bbaaaaabb")
print(data)