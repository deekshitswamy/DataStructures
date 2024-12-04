import io
from typing import List
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        for i in range(len(str1)):
            if j < len(str2):
                next_char = 'a' if str1[i] == 'z' else chr(ord(str1[i]) + 1)
                if str2[j] == str1[i] or str2[j] == next_char:
                    j += 1
        if j == len(str2):
            return True
        else:
            return False

obj = Solution()
#data = obj.canMakeSubsequence(str1 = "abc", str2 = "ad")
#data = obj.canMakeSubsequence(str1 = "zc", str2 = "ad")
data = obj.canMakeSubsequence(str1 = "ab", str2 = "d")
print(data)