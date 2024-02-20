class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i,cit in enumerate(citations):
            if i+1 > cit:
                return max(i,0)
        return len(citations)