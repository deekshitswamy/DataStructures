import io
from typing import List
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        if len(arr)<3:
            return 0
        self.maxlen=0
        self.se={}
        for i in range(len(arr)):
            self.se[arr[i]]=i
        def dp(pre1,pre2,curlen):
            if pre2==None:
                for i in range(pre1+1,len(arr)):
                    if arr[i]+arr[pre1] in self.se:
                        dp(pre1,i,curlen)
            if pre2!=None and arr[pre1]+arr[pre2] in self.se:
                idx=self.se[arr[pre1]+arr[pre2]]
                curlen+=1
                dp(pre2,idx,curlen)
                self.maxlen=max(curlen,self.maxlen)
        for i in range(len(arr)):
            dp(i,None,0)
        return self.maxlen+2 if self.maxlen!=0 else 0

obj = Solution()
#data = obj.lenLongestFibSubseq(arr = [1,2,3,4,5,6,7,8])
data = obj.lenLongestFibSubseq(arr = [1,3,7,11,12,14,18])
print(data)