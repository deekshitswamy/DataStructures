import io
from typing import List
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        char_maps = {}
        for i in range(len(s1)):
            c1, c2 = s1[i], s2[i]
            equivs = set([c1, c2])
            if c1 in char_maps:
                equivs |= char_maps[c1]
            if c2 in char_maps:
                equivs |= char_maps[c2]
            for c in equivs:
                char_maps[c] = equivs
        return "".join([
            min(char_maps[c]) if c in char_maps else c
            for c in baseStr
        ])

obj = Solution()
#data = obj.smallestEquivalentString(s1 = "parker", s2 = "morris", baseStr = "parser")
#data = obj.smallestEquivalentString(s1 = "hello", s2 = "world", baseStr = "hold")
data = obj.smallestEquivalentString(s1 = "leetcode", s2 = "programs", baseStr = "sourcecode")
print(data)