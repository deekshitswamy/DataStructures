import io
from typing import List
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)

        prev = [0 for j in range(l2+1)] 

        for i in range(1,l1+1):
            curr = [0 for x in range(l2+1)] 
            for j in range(1,l2+1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(curr[j-1], prev[j])
                
            prev = curr

        return curr[l2]

obj = Solution()
#data = obj.longestCommonSubsequence(text1 = "abcde", text2 = "ace")
#data = obj.longestCommonSubsequence(text1 = "abc", text2 = "abc")
data = obj.longestCommonSubsequence(text1 = "abc", text2 = "def")
print(data)