import io
from typing import List
from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counter):
            total = 0
            for ch in counter:
                if counter[ch] > 0:
                    counter[ch] -= 1  
                    total += 1 + backtrack(counter)  
                    counter[ch] += 1  
            return total
        
        
        return backtrack(Counter(tiles))

obj = Solution()
#data = obj.numTilePossibilities(tiles = "AAB")
#data = obj.numTilePossibilities(tiles = "AAABBC")
data = obj.numTilePossibilities(tiles = "V")
print(data)