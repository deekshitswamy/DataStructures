import io
from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        
        stack = []
        result = 0

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                idx = stack.pop()
                left_span = idx - stack[-1] if stack else idx + 1
                right_span = i - idx
                result = (result + arr[idx] * left_span * right_span) % MOD

            stack.append(i)

        while stack:
            idx = stack.pop()
            left_span = idx - stack[-1] if stack else idx + 1
            right_span = len(arr) - idx
            result = (result + arr[idx] * left_span * right_span) % MOD

        return result

obj = Solution()
#data = obj.sumSubarrayMins(arr = [3,1,2,4])
data = obj.sumSubarrayMins(arr = [11,81,94,43,3])
print(data)