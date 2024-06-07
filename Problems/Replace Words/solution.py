import io
from typing import List
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s=sentence.split(' ')
        n=len(s)
        d=dictionary
        ans=''
        for i in range(n):
            for j in d:
                m=len(j)
                if s[i][0:m]==j:
                    s[i]=j
        for i in s:
            ans+=i+' '
        return ans.strip()

obj = Solution()
#data = obj.replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery")
data = obj.replaceWords(dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs")
print(data)