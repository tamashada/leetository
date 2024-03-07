from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        c = l = len(ratings)
        mav = 1        
        ma = mi = 0
        for i in range(1,l):
            if ratings[i] > ratings[i-1]:
                ma = i
                mav = i-mi+1
                c += mav-1
            elif ratings[i] < ratings[i-1]:
                mi = i
                if i-ma < mav:
                    c += i-ma-1
                else:
                    c += i-ma
            else:
                ma = mi = i
                mav = 1
        return c