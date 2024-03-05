from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        al = k = sl = 0
        for i in range(len(gas)):
            d = gas[i] - cost[i]
            al += d
            if al < 0:     
                k = i+1
                sl += al
                al = 0
        return -1 if sl + al < 0 else k