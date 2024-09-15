import io
from typing import List
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = 0
        first_occurrence = {0: -1}  # base case for mask=0
        max_len = 0
        
        for i, char in enumerate(s):
            # Update the mask based on the current character
            if char == 'a':
                mask ^= 1
            elif char == 'e':
                mask ^= 2
            elif char == 'i':
                mask ^= 4
            elif char == 'o':
                mask ^= 8
            elif char == 'u':
                mask ^= 16

            # Check if this mask was seen before
            if mask in first_occurrence:
                max_len = max(max_len, i - first_occurrence[mask])
            else:
                first_occurrence[mask] = i  # store first occurrence of this mask
        
        return max_len

obj = Solution()
#data = obj.findTheLongestSubstring(s = "eleetminicoworoep")
#data = obj.findTheLongestSubstring(s = "leetcodeisgreat")
data = obj.findTheLongestSubstring(s = "bcbcbc")
print(data)