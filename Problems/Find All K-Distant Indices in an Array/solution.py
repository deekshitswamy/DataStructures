import io
from typing import List
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        stack = []
        for i in range(len(nums)):
            if nums[i] == key:
                if not stack:
                    stack.append([max(0, i-k), min(i+k, len(nums)-1)])
                else:
                    if stack[-1][-1] >= i-k:
                        stack[-1][-1] = min(i+k, len(nums)-1)
                    else:
                        stack.append([max(0, i-k), min(i+k, len(nums)-1)])
        ans = []
        for left, right in stack:
            while left <= right:
                ans.append(left)
                left += 1

        return ans

obj = Solution()
#data = obj.findKDistantIndices(nums = [3,4,9,1,3,9,5], key = 9, k = 1)
data = obj.findKDistantIndices(nums = [2,2,2,2,2], key = 2, k = 2)
print(data)