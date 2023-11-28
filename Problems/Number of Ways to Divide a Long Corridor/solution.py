import io
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod=10**9+7
        a,b,c=1,0,0
        for ch in corridor:
            if ch=="S":
                a,b,c=0,a+c,b
            else:
                a,b,c=a+c,b,c
        return c%mod

obj = Solution()
#data = obj.numberOfWays(corridor = "SSPPSPS")
#data = obj.numberOfWays(corridor = "PPSPSP")
data = obj.numberOfWays(corridor = "S")
print(data)