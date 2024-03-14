class Solution:
    def reverseWords(self, s: str) -> str:
        l = len(s)
        k = -1
        st = ''
        for i in range(l):
            if s[l-1-i] != ' ':
                if k == -1:
                    k = l-1-i
                if i == l-1:
                    st += f'{s[l-1-i:k+1]} '
            else:
                if k != -1:
                    st += f'{s[l-1-i+1:k+1]} '
                    k = -1        
        return st[:-1]