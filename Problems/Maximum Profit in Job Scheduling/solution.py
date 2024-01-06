import io
from typing import List
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        st = [(startTime[i],i) for i in range(n)]
        st.sort()

        dp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            next_profit = bisect.bisect_left(st,(endTime[st[i][1]],0),i+1)
            dp[i] = max(dp[i+1],profit[st[i][1]]+dp[next_profit])
        return dp[0]

obj = Solution()
#data = obj.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70])
#data = obj.jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60])
data = obj.jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4])
print(data)