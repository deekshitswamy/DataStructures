import io
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        temp_s = ''
        temp_g = ''
        c = 0
        if len(s) != len(goal):
            return False
        if s == goal and len(set(s)) < len(s):
            return True
        for i in range(len(s)):
            if s[i] != goal[i]:
                if c > 2 :
                    return False
                if c == 1 :
                    if s[i] != temp_g or goal[i] != temp_s:
                        return False
                temp_s = s[i]
                temp_g = goal[i]
                c += 1
        if c != 2:
            return False

        return True
            
obj = Solution()
# data = obj.buddyStrings(s = "ab", goal = "ba")
data = obj.buddyStrings(s = "ab", goal = "ab")
#data = obj.buddyStrings(s = "aa", goal = "aa")
print(data)