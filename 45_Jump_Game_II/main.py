from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        r = len(nums) - 1
        l = k = 0      
        while r > 0:
            k += 1
            while l + nums[l] < r:
                l += 1                 
            r = l
            l = 0
        return k  