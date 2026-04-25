class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1_count,s2_count = {},{}

        for i in range(len(s1)):
            s1_count[s1[i]] = 1+s1_count.get(s1[i],0)
            s2_count[s2[i]] = 1+s2_count.get(s2[i],0)
        
        if s1_count == s2_count:
            return True
        l=0
        for r in range(len(s1),len(s2)):
            s2_count[s2[r]] = 1+s2_count.get(s2[r],0)
            s2_count[s2[l]] -= 1
            if s2_count[s2[l]] <= 0:
                del s2_count[s2[l]]
            if s1_count == s2_count:
                return True
            l+=1
        return False