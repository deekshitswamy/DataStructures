import io
from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivot_count = 0
        less, equal, more = [], [], []

        for num in nums:
            if num == pivot:
                equal.append(num)
            elif num < pivot:
                less.append(num)
            else:
                more.append(num)

        return (less + equal + more)

obj = Solution()
#data = obj.pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10)
data = obj.pivotArray(nums = [-3,4,3,2], pivot = 2)
print(data)