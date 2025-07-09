import io
from typing import List
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        ans = 0
        start,end,meetingSum,n = 0,0,0,len(startTime)
        for i in range(n):
            meetingSum += endTime[i] - startTime[i]
            end = startTime[i+1] if i + 1 < n else eventTime
            if i >= k:
                meetingSum -= endTime[i-k] - startTime[i-k]
                start = endTime[i-k]
            ans = max(ans,end - start - meetingSum)
        return ans

obj = Solution()
#data = obj.maxFreeTime(eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5])
#data = obj.maxFreeTime(eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10])
data = obj.maxFreeTime(eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5])
print(data)