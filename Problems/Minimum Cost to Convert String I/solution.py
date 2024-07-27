import io
from typing import List
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        pass

obj = Solution()
#data = obj.minimumCost(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20])
#data = obj.minimumCost(source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2])
data = obj.minimumCost(source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000])
print(data)