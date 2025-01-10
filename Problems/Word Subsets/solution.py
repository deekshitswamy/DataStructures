import io
from typing import List
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        map = [0] * 26
        for x in words2:
            temp = [0] * 26
            for c in x:
                temp[ord(c) - ord('a')] += 1
            for i in range(26):
                map[i] = max(map[i], temp[i])
        ans = []
        for i in words1:
            temp = [0] * 26
            for c in i:
                temp[ord(c) - ord('a')] += 1
            if all(temp[j] >= map[j] for j in range(26)):
                ans.append(i)
        return ans

obj = Solution()
#data = obj.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"])
data = obj.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"])
print(data)