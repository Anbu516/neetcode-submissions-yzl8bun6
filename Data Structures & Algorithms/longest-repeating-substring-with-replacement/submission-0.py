class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = r =0
        c = {}
        m=0
        while r<len(s):
            c[s[r]] = 1+c.get(s[r],0)
            if (r-l+1) - max(c.values()) > k:
                c[s[l]] -= 1
                l+=1
            res = max(res,r-l+1,res)
            r+=1
        return res