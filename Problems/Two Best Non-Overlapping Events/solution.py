import io
from typing import List
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        pq = []
        max_val = 0
        ans = 0

        for start, end, value in events:
            while pq and pq[0][0] < start:
                max_val = max(max_val, heapq.heappop(pq)[1])
            ans = max(ans, max_val + value)
            heapq.heappush(pq, (end, value))

        return ans

obj = Solution()
#data = obj.maxTwoEvents(events = [[1,3,2],[4,5,2],[2,4,3]])
#data = obj.maxTwoEvents(events = [[1,3,2],[4,5,2],[1,5,5]])
data = obj.maxTwoEvents(events = [[1,5,3],[1,5,1],[6,6,5]])
print(data)