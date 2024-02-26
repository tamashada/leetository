from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        lv = nums[0]
        rv = nums[l-1]
        answer = [1]*l
        for i in range(l-1):
            answer[i+1] *= lv
            lv *= nums[i+1]
            answer[l-2-i] *= rv
            rv *= nums[l-2-i]
        return answer