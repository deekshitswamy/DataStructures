import io

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1 or n==0:
            return 0
        length=1<<n-1
        mid=length //2
        if k<=mid:
            return self.kthGrammar(n-1,k)
        else:
            return  (int(not(self.kthGrammar(n-1,k-mid))))

obj = Solution()
#data = obj.kthGrammar(n = 1, k = 1)
#data = obj.kthGrammar(n = 2, k = 1)
data = obj.kthGrammar(n = 2, k = 2)
print(data)