import io
from typing import List
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sum_ = sum(skill)
        n = len(skill)
        if n == 2:
            return skill[0] * skill[1]
        if sum_ % (n//2) != 0:
            return -1
        skill.sort()
        score = skill[0] + skill[-1]
        pairs = []
        result = 0
        for i in range(n // 2):
            l, r = skill[i], skill[n - 1 - i]
            if l + r != score:
                return -1
            result += l * r
        return result

obj = Solution()
#data = obj.dividePlayers(skill = [3,2,5,1,3,4])
#data = obj.dividePlayers(skill = [3,4])
data = obj.dividePlayers(skill = [1,1,2,3])
print(data)