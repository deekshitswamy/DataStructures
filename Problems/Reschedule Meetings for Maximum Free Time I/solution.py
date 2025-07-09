import io
from typing import List
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        pass

obj = Solution()
#data = obj.maxFreeTime(eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5])
#data = obj.maxFreeTime(eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10])
data = obj.maxFreeTime(eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5])
print(data)