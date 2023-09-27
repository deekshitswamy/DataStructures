import io
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        n=len(s)
        i=0
        count=0
        while i<n:
            if s[i].isnumeric():
                if (int(s[i])-1)*count>=k:
                    i=0
                    count=0
                    continue
                else:
                    k-=(int(s[i])-1)*count
                    count+=(int(s[i])-1)*count
            else:
                k-=1
                count+=1
                if k==0:
                    return s[i]
            i+=1 

obj = Solution()
#data = obj.decodeAtIndex(s = "leet2code3", k = 10)
#data = obj.decodeAtIndex(s = "ha22", k = 5)
data = obj.decodeAtIndex(s = "a2345678999999999999999", k = 1)
print(data)