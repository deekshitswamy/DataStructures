import io
from typing import List
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff_array = [0] * (n+1) 

        for start, end in queries:
            diff_array[start] += 1
            if end + 1 < n:
                diff_array[end + 1] -= 1

        current = 0
        for index in range(n):
            current += diff_array[index]
            if nums[index] > current:
                return False

        return True

obj = Solution()
#data = obj.isZeroArray(nums = [1,0,1], queries = [[0,2]])
data = obj.isZeroArray(nums = [4,3,2,1], queries = [[1,3],[0,2]])
print(data)