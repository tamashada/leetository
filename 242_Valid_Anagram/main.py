class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        l = len(s)
        if l != len(t):
            return False
        ms = {}
        mt = {}
        for i in range(l):
            ms[s[i]] = 1 + ms.get(s[i],0)
            mt[t[i]] = 1 + mt.get(t[i],0)
        return ms == mt
    
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
          return sorted(s) == sorted(t)