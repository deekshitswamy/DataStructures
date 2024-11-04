import io
from typing import List
from collections import defaultdict
class Solution:
    def compressedString(self, word: str) -> str:
        dic = defaultdict(int)
        res = []
        prev = ""

        for i in word: 
            dic[i] += 1
            if prev == i and dic[i] < 9 : 
                continue
            else:
                if prev == i and dic[i] == 9: 
                    res.append("9"+i)
                    dic[i] = 0 
                if prev != i and dic[prev] != 0: 
                    val = str(dic[prev])
                    res.append(val+prev)
                    dic = defaultdict(int)
                    dic[i] += 1
            prev = i
        if dic[word[-1]] < 9 and dic[word[-1]] != 0: 
            s = str(dic[word[-1]])
            res.append(s+word[-1])
        return "".join(res)

obj = Solution()
#data = obj.compressedString(word = "abcde")
data = obj.compressedString(word = "aaaaaaaaaaaaaabb")
print(data)