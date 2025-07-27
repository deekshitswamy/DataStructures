import io
from typing import List
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        stack = []
        result = 0

        for num in nums:
            if stack and stack[-1] == num:
                continue
            stack.append(num)

        print(stack)
        
        for i in range(1,len(stack)-1):
            if stack[i-1]< stack[i] > stack[i+1]:
                result += 1
            elif stack[i-1] > stack[i] < stack[i+1]:
                result += 1
        return result

obj = Solution()
#data = obj.countHillValley(nums = [2,4,1,1,6,5])
data = obj.countHillValley(nums = [6,6,5,5,4,1])
print(data)