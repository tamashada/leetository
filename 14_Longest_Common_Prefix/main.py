from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        k = len(pre)
        for i in range(1,len(strs)):
            if len(strs[i]) < k:
                k = len(strs[i])
            for j in range(k):
                if strs[i][j] != pre[j]:
                    k = j
                    break
        return pre[:k] if k >= 0 else ""