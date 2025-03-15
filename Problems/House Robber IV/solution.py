import io
from typing import List
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        ln = len(nums)

        def helper(n):
            total = 0
            i = 0
            while i < ln:
                if nums[i] > n:
                    i += 1
                    continue
                j = i
                while j < ln and nums[j] <= n:
                    j += 1
                lng = j - i
                if lng % 2 == 0:
                    total += (lng // 2)
                else:
                    total = total + (lng // 2) + 1
                i = j
            return True if total >= k else False
        
        s, e = 0, max(nums)
        while s != e - 1 and s < e:
            mid = (s + e) // 2
            if helper(mid):
                e = mid
            else:
                s = mid
        nums.sort()
        for i in nums:
            if i >= e:
                return i

obj = Solution()
#data = obj.minCapability(nums = [2,3,5,9], k = 2)
data = obj.minCapability(nums = [2,7,9,3,1], k = 2)
print(data)