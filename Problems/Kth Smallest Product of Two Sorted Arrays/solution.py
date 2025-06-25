import io
from typing import List
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def valid_pairs(x):
            count = 0
            for num in nums1:
                if num > 0:
                    count += bisect_right(nums2, x // num)
                elif num < 0:
                    count += len(nums2) - bisect_left(nums2, ceil(x / num))
                elif num == 0 and x >= 0:
                    count += len(nums2)
            return count

        low, high = -10**10 - 1, 10**10 + 1

        while low + 1 < high:
            mid = (low + high) // 2
            if valid_pairs(mid) >= k:
                high = mid
            else:
                low = mid

        return low + 1

obj = Solution()
#data = obj.kthSmallestProduct(nums1 = [2,5], nums2 = [3,4], k = 2)
#data = obj.kthSmallestProduct(nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6)
data = obj.kthSmallestProduct(nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3)
print(data)