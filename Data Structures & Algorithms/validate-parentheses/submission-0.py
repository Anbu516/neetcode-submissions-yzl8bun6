class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i==')' and l and l[-1]=='(':
                l.pop()
            elif i=='}' and l and l[-1]=='{':
                l.pop()
            elif i==']' and l and l[-1]=='[':
                l.pop()
            else:
                l.append(i)
        if not l:
            return True
        else:
            return False