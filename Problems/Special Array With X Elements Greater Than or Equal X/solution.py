import io
from typing import List
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        greater_number_count = defaultdict(int)
        for num in nums:
            greater_number_count[min(len(nums), num)] += 1
        
        curr_count = 0
        for i in range(len(nums), -1, -1):
            x = greater_number_count[i] + curr_count
            if i == x:
                return i
            curr_count += greater_number_count[i]
        
        return -1

obj = Solution()
#data = obj.specialArray(nums = [3,5])
#data = obj.specialArray(nums = [0,0])
data = obj.specialArray(nums = [0,4,3,0,4])
print(data)