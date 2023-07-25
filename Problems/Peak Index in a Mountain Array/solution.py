import io
from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] < arr[mid + 1]:
                # We are on the ascending slope of the mountain.
                # Move the left pointer to mid + 1.
                left = mid + 1
            else:
                # We are on the descending slope of the mountain.
                # Move the right pointer to mid.
                right = mid

        # The left pointer will be at the peak of the mountain.
        return left

obj = Solution()
data = obj.peakIndexInMountainArray(arr = [0,1,0])
#data = obj.peakIndexInMountainArray(arr = [0,2,1,0])
#data = obj.peakIndexInMountainArray(arr = [0,10,5,2])
print(data)