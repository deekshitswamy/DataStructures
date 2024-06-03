import io
from typing import List
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_index = 0
        t_index = 0
        nomatch = False
        for i in range(t_index, len(t)):
            #print("t=====>",t[i],end=",")
            for j in range(s_index, len(s)):
                #print("\ns=>",s[j],end="")
                nomatch = True
                if t[i] == s[j]:
                    t_index = i+1
                    s_index = j+1
                    nomatch = False
                    break
            if nomatch:
                break
            print()
        return len(t[t_index:])

obj = Solution()
#data = obj.appendCharacters(s = "coaching", t = "coding")
#data = obj.appendCharacters(s = "abcde", t = "a")
data = obj.appendCharacters(s = "z", t = "abcde")
print(data)