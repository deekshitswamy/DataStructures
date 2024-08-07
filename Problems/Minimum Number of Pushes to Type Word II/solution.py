import io
from typing import List
class Solution:
    def minimumPushes(self, word: str) -> int:
        d={}
        for i in set(word):
            d[i]=word.count(i)
        print(d)
        dd=sorted(d.items(),key=lambda x:x[1],reverse=True)
        print(dd)
        c=0
        j=1
        x=1
        for i in dd:
            c+=i[1]*x
            j+=1
            if j>8:
                j=1
                x+=1
        return c

obj = Solution()
#data = obj.minimumPushes(word = "abcde")
#data = obj.minimumPushes(word = "xyzxyzxyzxyz")
data = obj.minimumPushes(word = "aabbccddeeffgghhiiiiii")
print(data)