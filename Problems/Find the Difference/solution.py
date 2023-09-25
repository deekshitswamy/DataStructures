import io
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        b = 0
        s = s+t
        for c in s:
            b = b ^ ord(c)
        return chr(b)

obj = Solution()
#data = obj.findTheDifference(s = "abcd", t = "abcde")
data = obj.findTheDifference(s = "", t = "y")
print(data)