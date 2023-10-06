import io
class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        ans=1
        while n>4:
            ans=ans*3
            n-=3
        return ans*n 

obj = Solution()
#data = obj.integerBreak(n = 2)
data = obj.integerBreak(n = 10)
print(data)