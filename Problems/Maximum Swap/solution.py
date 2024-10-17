import io
from typing import List
class Solution:
    def maximumSwap(self, num: int) -> int:
        n = str(num)
        l = list(n)
        length = len(l)
        
        # Iterate through the list
        for i in range(length):
            # Only proceed if there are elements after l[i]
            if i + 1 < length and l[i] < max(l[i+1:]):
                # Find the max number in the rest of the list
                m = max(l[i+1:])
                # Find the index of that max number, in the context of the whole list
                idx = len(l) - 1 - l[::-1].index(m)
                # Swap the values
                l[i], l[idx] = l[idx], l[i]
                break
        
        # Return the modified list as an integer
        return int(''.join(l))

obj = Solution()
#data = obj.maximumSwap(num = 2736)
data = obj.maximumSwap(num = 9973)
print(data)