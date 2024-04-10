import io
from typing import List
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ans=[]
        deck.sort(reverse=True)
        for i in deck:
            ans=[i]+ans[-1:]+ans[:-1]
        return ans

obj = Solution()
#data = obj.deckRevealedIncreasing(deck = [17,13,11,2,3,5,7])
data = obj.deckRevealedIncreasing(deck = [1,1000])
print(data)