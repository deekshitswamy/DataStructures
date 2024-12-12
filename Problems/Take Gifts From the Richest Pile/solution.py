import io
from math import sqrt
from typing import List
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k:
            gifts.sort(reverse=True)
            pile = gifts[0]
            gifts.pop(0)
            gifts.append(int(sqrt(pile)))
            k -= 1
        return sum(gifts)

obj = Solution()
#data = obj.pickGifts(gifts = [25,64,9,4,100], k = 4)
data = obj.pickGifts(gifts = [1,1,1,1], k = 4)
print(data)