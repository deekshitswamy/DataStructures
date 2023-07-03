# Valid Palindrome
import io
class Solution:
    def isPalindrome(self, s: str)->bool:
        s = self.getAlphaNum(s)
        n = len(s)//2
        for i in range(n):
            if s[i] != s[-i-1]:
                return False
        return True
    def getAlphaNum(self, s: str)->str:
        alpha_s = []
        for i in s:
            if i.isalnum():
                alpha_s.append(i)
        return "".join(alpha_s)

obj = Solution()
data = obj.isPalindrome(s="helloo@olleh")
print(data)