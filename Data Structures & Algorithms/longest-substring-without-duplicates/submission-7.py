class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,1
        m = 0
        if len(s) == 0:
            return 0
        d={s[l]:1}
        if len(s) == 1:
            return 1
        while r < len(s):
            if s[l]==s[r]:
                m = max(m,len(s[l:r]))
                l+=1
                r+=1
            else:
                if s[r] in d:
                    m = max(m,len(d))
                    l=r
                    d={}
                d[s[r]] = 1
                r+=1
        m = max(m,len(d))
        return m