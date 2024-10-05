import io
from typing import List
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        tsum = sum(skill)
        tsum = (tsum / len(skill)) * 2

        mp = {}
        for x in skill:
            mp[x] = mp.get(x, 0) + 1

        chem = 0
        for key in list(mp.keys()):
            val = mp[key]
            complement = tsum - key

            if complement not in mp or val != mp[complement]:
                return -1

            if key == complement:
                chem += (key * complement) * (val / 2)
            else:
                chem += (key * complement) * val

            del mp[key]
            del mp[complement]

        return chem

obj = Solution()
#data = obj.dividePlayers(skill = [3,2,5,1,3,4])
#data = obj.dividePlayers(skill = [3,4])
data = obj.dividePlayers(skill = [1,1,2,3])
print(data)