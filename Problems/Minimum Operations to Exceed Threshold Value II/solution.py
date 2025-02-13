import io
from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        pq = [num for num in nums]
        heapq.heapify(pq)
        cnt = 0

        while len(pq) > 1 and pq[0] < k:
            x = heapq.heappop(pq)
            y = heapq.heappop(pq)
            newEle = min(x, y) * 2 + max(x, y)
            heapq.heappush(pq, newEle)
            cnt += 1

        return cnt if pq[0] >= k else -1

obj = Solution()
#data = obj.minOperations(nums = [2,11,10,1,3], k = 10)
data = obj.minOperations(nums = [1,1,2,4,9], k = 20)
print(data)