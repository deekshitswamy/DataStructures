import io
from typing import List
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # We collect and sort the value of all n - 1 pairs.
        n = len(weights)
        pair_weights = [0] * (n - 1)
        for i in range(n - 1):
            pair_weights[i] = weights[i] + weights[i + 1]
        pair_weights.sort()
        
        # Get the difference between the largestk - 1  values and the 
        # smallest k - 1 values.
        ans = 0
        for i in range(k - 1):
            ans += pair_weights[n - 2 - i] - pair_weights[i]
            
        return ans

obj = Solution()
data = obj.putMarbles(weights = [1,3,5,1], k = 2)
#data = obj.putMarbles(weights = [1, 3], k = 2)
print(data)