import io
class Solution:
    def minFlips(self, target: str) -> int:
        init_str = "0"*len(target)
        count = 0
        for i in range(len(target)):
            if target[i] == init_str[i]:
                continue
            else:
                init_str = init_str[:i+1] + (target[i])*(len(init_str)-i-1)
                count += 1
        return count

obj = Solution()
#data = obj.minFlips(target = "10111")
data = obj.minFlips(target = "101")
print(data)