class Solution:
    def intToRoman(self, num: int) -> str:
        num = str(num)
        chs_l = ['I','X','C','M']
        chs_h = ['V','L','D']
        l = len(num)
        su = ''
        for i in range(l):
            n = int(num[l-1-i])
            if n < 5:
                if n == 4:
                    su = chs_l[i] + chs_h[i] + su
                else:
                    su = chs_l[i] * n + su
            else:
                if n == 9:
                    su = chs_l[i] + chs_l[i+1] + su
                else:
                    su = chs_h[i] + chs_l[i] * (n-5) + su
        return su