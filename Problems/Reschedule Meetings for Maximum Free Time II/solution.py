import io
from typing import List
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        pass

obj = Solution()
#data = obj.maxFreeTime(eventTime = 5, startTime = [1,3], endTime = [2,5])
#data = obj.maxFreeTime(eventTime = 10, startTime = [0,7,9], endTime = [1,8,10])
#data = obj.maxFreeTime(eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10])
data = obj.maxFreeTime(eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5])
print(data)