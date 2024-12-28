import io
from typing import List
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        vals = self.get_vals(nums, k)
        l, r = self.rec(nums, 3, 0, k, vals, dict())
        return l

    def rec(self, nums, left, i, k, vals, d):
        key = i, left
        if key in d: return d[key]

        n = len(nums)

        if left == 0 or i not in vals: return [], 0

        lst_take, res_take = self.rec(nums, left-1, i+k, k, vals, d)
        res_take += vals[i]

        lst, res = self.rec(nums, left, i+1, k, vals, d)

        if res_take >= res:
            res = res_take
            lst = [i]+lst_take
        d[key] = (lst, res)
        return d[key]

    def get_vals(self, nums, k):
        d = dict()
        n = len(nums)
        d[0] = sum(nums[:k])
        for end in range(k, n):
            d[end-k+1] = d[end-k]-nums[end-k]+nums[end]
        return d

obj = Solution()
#data = obj.maxSumOfThreeSubarrays(nums = [1,2,1,2,6,7,5,1], k = 2)
data = obj.maxSumOfThreeSubarrays(nums = [1,2,1,2,1,2,1,2,1], k = 2)
print(data)