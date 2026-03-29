class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        s = list(s1)
        for i,j in [(0,2),(1,3)]:
            s[i], s[j] = s[j], s[i]
            if "".join(s) == s2:
                return True

        s = list(s1)
        for i,j in [(1,3),(0,2)]:
            s[i], s[j] = s[j], s[i]
            if "".join(s) == s2:
                return True
        return False
