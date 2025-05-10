import io
from typing import List
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        num_zero1 = nums1.count(0)
        num_zero2 = nums2.count(0)
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        min_sum1 = sum1 + num_zero1
        min_sum2 = sum2 + num_zero2

        if num_zero1 == num_zero2 == 0:
            return sum1 if sum1 == sum2 else -1
        elif num_zero1 == 0:
            return sum1 if sum1 >= min_sum2 else -1
        elif num_zero2 == 0:
            return sum2 if sum2 >= min_sum1 else -1
        
        min_sum = max(min_sum1, min_sum2)

        return min_sum if min_sum1 + min_sum2 != 0 else -1

obj = Solution()
#data = obj.minSum(nums1 = [3,2,0,1,0], nums2 = [6,5,0])
data = obj.minSum(nums1 = [2,0,2,0], nums2 = [1,4])
print(data)