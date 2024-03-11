class Solution:
    def romanToInt(self, s: str) -> int:
        chars = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        schars = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        su = 0
        i = 0
        while i < len(s):
            n = chars[s[i]]            
            if i < len(s)-1 and s[i:i+2] in schars:
                n = chars[s[i+1]] - n
                i += 1
            su += n
            print(su)
            i += 1
        return su