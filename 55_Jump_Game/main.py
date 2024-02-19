from typing import List, Dict

# Optimal O(N) - O(1)
class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        l = r = len(nums)-1
        k = 0
        while r > 0:
            r -= 1
            if nums[r] == 0:
                k += 1
            else:                
                if k > 0:
                    l = r
                    lmin = -1
                    while l >= 0:                        
                        if l + nums[l] > r + k:
                            lmin = l
                        l -= 1
                    if lmin == -1:
                        return False    
                    else:
                        l = r = lmin
                        k = 0
        return k == 0

# Recursive, not bruteforce
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        return self._canJump(nums, 0, len(nums), dict())
    def _canJump(self, nums: List[int], i: int, l: int, cache: Dict[int, bool]) -> bool:
        if i in cache:
            return cache[i]
        print(f'i: {i}, nums[i]: {nums[i]}')
        index = nums[i] + i
        if index >= l-1:
            cache[index] = True
            return True
        while index > i:
            can = self._canJump(nums, index, l, cache)
            if can:
                cache[index] = True
                return True
            index -= 1
        cache[index] = False
        return False