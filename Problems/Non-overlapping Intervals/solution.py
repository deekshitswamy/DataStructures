import io
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        ans=0
        prevEnd=intervals[0][1]
        for start,end in intervals[1:]:
            if start>=prevEnd:
                prevEnd=end
            else:
                ans+=1
                prevEnd=min(end,prevEnd) 
        return ans

obj = Solution()
data = obj.eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]])
#data = obj.eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]])
#data = obj.eraseOverlapIntervals(intervals = [[1,2],[2,3]])
print(data)