import io
from typing import List
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        res, prev = 0, 0
        for start, end in meetings:
            res += max(0, start - prev - 1)
            prev = max(end, prev)
        res += max(0, days - prev)
        return res

obj = Solution()
#data = obj.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]])
#data = obj.countDays(days = 5, meetings = [[2,4],[1,3]])
data = obj.countDays(days = 6, meetings = [[1,6]])
print(data)