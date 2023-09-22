import io
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x=iter(t)
        return all(ch in x for ch in s)

obj = Solution()
#data = obj.isSubsequence(s = "abc", t = "ahbgdc")
data = obj.isSubsequence(s = "axc", t = "ahbgdc")
print(data)