import io
from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums_set = set()
        current_sum = max_sum = begin = 0

        for end in range(n):
            if nums[end] not in nums_set:
                current_sum += nums[end]
                nums_set.add(nums[end])

                if end - begin + 1 == k:
                    if current_sum > max_sum:
                        max_sum = current_sum

                    current_sum -= nums[begin]
                    nums_set.remove(nums[begin])
                    begin += 1
            else:
                while nums[begin] != nums[end]:
                    current_sum -= nums[begin]
                    nums_set.remove(nums[begin])
                    begin += 1

                begin += 1

        return max_sum

obj = Solution()
#data = obj.maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3)
data = obj.maximumSubarraySum(nums = [4,4,4], k = 3)
print(data)