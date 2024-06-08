import io
from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        Sliding window solution will not work here 
        This solution reqired different point of view to solve the problem 
        Using hashmap to store the reminder and making the count for the inside
        to handle the edge case have an 0 key will value of -1 since the length of the 
        hashmap should be 2
        '''

        hash_map = { 0 : -1}
        total = 0
        for i ,value in enumerate(nums):
            total +=value
            reminder = total % k 

            if reminder not in hash_map:
                hash_map[reminder] = i
            elif i - hash_map[reminder]>1:
                return True
        return False

obj = Solution()
#data = obj.checkSubarraySum(nums = [23,2,4,6,7], k = 6)
#data = obj.checkSubarraySum(nums = [23,2,6,4,7], k = 6)
data = obj.checkSubarraySum(nums = [23,2,6,4,7], k = 13)
print(data)