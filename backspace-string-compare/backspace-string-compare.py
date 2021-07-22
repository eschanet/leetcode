class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        exclude = lambda s, i: s[:max(i,0)] + s[min(i+2,len(s)):]
        
        s, t = s[::-1], t[::-1]
        for i in range(len(s)-1, -1, -1):
            if s[i] == '#':
                s = exclude(s,i)

        for i in range(len(t)-1, -1, -1):
            if t[i] == '#':
                t = exclude(t,i)
        
        return s == t    