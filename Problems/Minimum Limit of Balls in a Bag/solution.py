import io
from typing import List
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            ops = 0

            for n in nums:
                ops += (n - 1) // mid
                if ops > maxOperations:
                    break

            if ops <= maxOperations:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

obj = Solution()
#data = obj.minimumSize(nums = [9], maxOperations = 2)
data = obj.minimumSize(nums = [2,4,8,2], maxOperations = 4)
print(data)