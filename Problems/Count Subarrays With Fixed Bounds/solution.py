import io
from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        cnt = 0
        last_minK_pos, last_maxK_pos = None, None
        last_violating_position = -1

        for i, num in enumerate(nums):
            if num > maxK or num < minK:
                last_minK_pos, last_maxK_pos = None, None
                last_violating_position = i
            elif minK < num and num < maxK:
                if last_minK_pos is None or last_maxK_pos is None:
                    pass
                else:
                    last = min(last_minK_pos, last_maxK_pos) - last_violating_position
                    cnt += last
            else:
                if num == maxK:
                    last_maxK_pos = i
                if num == minK:
                    last_minK_pos = i

                if last_minK_pos is not None and last_maxK_pos is not None:
                    last = min(last_minK_pos, last_maxK_pos) - last_violating_position
                    cnt += last
 
        return cnt

obj = Solution()
#data = obj.countSubarrays(nums = [1,3,5,2,7,5], minK = 1, maxK = 5)
data = obj.countSubarrays(nums = [1,1,1,1], minK = 1, maxK = 1)
print(data)