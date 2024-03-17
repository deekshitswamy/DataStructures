import io
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        pass

obj = Solution()
#data = obj.insert(intervals = [[1,3],[6,9]], newInterval = [2,5])
data = obj.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8])
print(data)