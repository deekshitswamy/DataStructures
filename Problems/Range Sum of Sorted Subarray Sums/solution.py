import io
import heapq
from typing import List
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        minHeap = [(n, i) for i, n in enumerate(nums)]
        res = 0
        MOD = 10 ** 9 + 7
        heapq.heapify(minHeap)

        for i in range(right):
            num, index = heapq.heappop(minHeap)
            if i >= left - 1:
                res = (res + num) % MOD
            if index + 1 < n:
                next = (num + nums[index+1], index + 1)
                heapq.heappush(minHeap, next)

        return res

obj = Solution()
#data = obj.rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 5)
#data = obj.rangeSum(nums = [1,2,3,4], n = 4, left = 3, right = 4)
data = obj.rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 10)
print(data)