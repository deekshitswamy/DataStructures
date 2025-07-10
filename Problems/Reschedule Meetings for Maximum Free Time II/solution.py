import io
from typing import List
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [startTime[0]]
        gaps += [start-p_end for start,p_end in zip(startTime[1:], endTime)]
        gaps.append(eventTime - endTime[-1])

        maxGapLeft, maxGapRight = [0]*(n+1), [0]*(n+1)
        for i in range(n+1):
            maxGapLeft[i] = gaps[i] if i==0 else max(gaps[i], maxGapLeft[i-1])
        for i in range(n,-1,-1):
            maxGapRight[i] = gaps[i] if i == n else max(gaps[i], maxGapRight[i+1])

        res = 0

        for i in range(n):
            maxGap = gaps[i]+gaps[i+1]
            duration = endTime[i]-startTime[i]
            if (i-1>=0 and maxGapLeft[i-1] >= duration) or (i+2<=n and maxGapRight[i+2] >= duration):
                maxGap += duration
            res = max(res, maxGap)
        return res

obj = Solution()
#data = obj.maxFreeTime(eventTime = 5, startTime = [1,3], endTime = [2,5])
#data = obj.maxFreeTime(eventTime = 10, startTime = [0,7,9], endTime = [1,8,10])
#data = obj.maxFreeTime(eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10])
data = obj.maxFreeTime(eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5])
print(data)