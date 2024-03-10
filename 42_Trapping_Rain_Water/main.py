from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l = lm = rm = s = 0
        r = len(height)-1
        while l <= r:
            lv = height[l]
            rv = height[r]            
            if lm <= rm:
                lm = max(lv, lm)
                s += max(min(lm,rm)-lv,0)
                l += 1
            else:
                rm = max(rv, rm)
                s += max(min(lm,rm)-rv,0)
                r -= 1
        return s