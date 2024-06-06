import io
from typing import List
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        nums.sort()
        count = Counter(nums)
        
        for card in nums:
            if count[card] == 0:
                continue
            for i in range(k):
                if count[card + i] > 0:
                    count[card + i] -= 1
                else:
                    return False
        return True

obj = Solution()
#data = obj.isPossibleDivide(nums = [1,2,3,3,4,4,5,6], k = 4)
#data = obj.isPossibleDivide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3)
data = obj.isPossibleDivide(nums = [1,2,3,4], k = 3)
print(data)