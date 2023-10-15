import io
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod=10**9+7
        n=min(arrLen,steps//2+1)
        ways=[1]+[0]*(n-1)
        for step in range(steps):
            ways=[sum(ways[max(0,i-1):i+2])%mod for i in range(min(step+2,steps-step,n))]
        return ways[0] 

obj = Solution()
#data = obj.numWays(steps = 3, arrLen = 2)
data = obj.numWays(steps = 2, arrLen = 4)
print(data)