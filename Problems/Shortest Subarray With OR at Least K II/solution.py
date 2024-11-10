import io
from collections import Counter
from typing import List
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def get_bits(elem):
            result = []
            value = 1
            while elem:
                if elem % 2:
                    result.append(value)
                elem //= 2
                value *= 2
            return result
        
        left = 0
        result = float('inf')
        state = Counter()
        state_value = 0

        for right, elem in enumerate(nums):
            # update state with right element
            for value in get_bits(elem):
                if state[value] == 0:
                    state_value += value
                state[value] += 1
            
            while left < right:
                elem_values = get_bits(nums[left])
                
                # check left element
                delta = sum(
                    value
                    for value in elem_values
                    if state[value] == 1
                )
                if state_value - delta < k:
                    break
                left += 1

                # update state without left element
                for value in elem_values:
                    state[value] -= 1
                state_value -= delta
            
            # update answer
            if state_value >= k:
                result = min(result, right - left + 1)

        if result == float('inf'):
            return -1
        return result
    
obj = Solution()
#data = obj.minimumSubarrayLength(nums = [1,2,3], k = 2)
#data = obj.minimumSubarrayLength(nums = [2,1,8], k = 10)
data = obj.minimumSubarrayLength(nums = [1,2], k = 0)
print(data)