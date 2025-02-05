import io
from typing import List
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        not_match, count = -1, 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if count == 2:
                    return False
                elif not_match == -1:
                    not_match = i
                elif s1[not_match] != s2[i] or s1[i] != s2[not_match]:
                    return False
                count += 1
        return count == 0 or count == 2

obj = Solution()
#data = obj.areAlmostEqual(s1 = "bank", s2 = "kanb")
#data = obj.areAlmostEqual(s1 = "attack", s2 = "defend")
data = obj.areAlmostEqual(s1 = "kelb", s2 = "kelb")
print(data)