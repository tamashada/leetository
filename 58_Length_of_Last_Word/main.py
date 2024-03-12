class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)
        ien = -1
        ist = l
        for i in range(l):
            if s[l-1-i] != ' ':
                if ien == -1:
                    ien = i
            else:
                if ien != -1:
                    ist = i
                    break
        return ist-ien