import io
import math
from typing import List
class Solution:
    def minSwaps(self, s: str) -> int:
        st = [] # Stack to track unbalanced parentheses
        
        for i in s:
            if i == '[':
                st.append(i) # Push opening bracket to the stack
            elif st and st[-1] == '[':
                st.pop() # Excluding balanced pairs
            else:
                st.append(i) # Push closing bracket to the stack
        
        unbalancedPairs = len(st) // 2
        swaps = math.ceil(unbalancedPairs / 2.0)
        return swaps

obj = Solution()
#data = obj.minSwaps(s = "][][")
#data = obj.minSwaps(s = "]]][[[")
data = obj.minSwaps(s = "[]")
print(data)