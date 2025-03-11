import io
from typing import List
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ls = [-1, -1, -1]  
        count = 0  
        for i in range(len(s)):  
            ls[ord(s[i]) - ord('a')] = i  
            if -1 not in ls:  
                count += 1 + min(ls)  
        return count

obj = Solution()
#data = obj.numberOfSubstrings(s = "abcabc")
#data = obj.numberOfSubstrings(s = "aaacb")
data = obj.numberOfSubstrings(s = "abc")
print(data)