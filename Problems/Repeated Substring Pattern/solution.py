import io
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ds=(s+s)[1:-1]
        return s in ds

obj = Solution()
#data = obj.repeatedSubstringPattern(s = "abab")
#data = obj.repeatedSubstringPattern(s = "aba")
data = obj.repeatedSubstringPattern(s = "abcabcabcabc")
print(data)