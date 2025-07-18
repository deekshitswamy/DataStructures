import io
import heapq
from typing import List
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        pq_mx = [-nums[i] for i in range(n)]
        heapq.heapify(pq_mx)
        mn_ss = -sum(pq_mx)
        mn_arr = [mn_ss] * (n+1)

        for i in range(n, 2*n):
            if nums[i] < -pq_mx[0]:
                mx = heapq.heapreplace(pq_mx, -nums[i])
                mn_ss += mx + nums[i]
            
            mn_arr[i-n + 1] = mn_ss

        pq_mn = [nums[i] for i in range(2*n, 3*n)]
        heapq.heapify(pq_mn)
        mx_ss = sum(pq_mn)
        mx_arr = [mx_ss] * (n+1)

        for i in range(2*n - 1, n-1, -1):
            if nums[i] > pq_mn[0]:
                mn = heapq.heapreplace(pq_mn, nums[i])
                mx_ss += -mn + nums[i]
            
            mx_arr[i-n] = mx_ss

        return min(mn-mx for mn, mx in zip(mn_arr, mx_arr))

obj = Solution()
#data = obj.minimumDifference(nums = [3,1,2])
data = obj.minimumDifference(nums = [7,9,5,8,1,3])
print(data)