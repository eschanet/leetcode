class Solution:
    def romanToInt(self, s: str) -> int:
        to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        n,i = 0,0
        while i < len(s):
            if (i+1 < len(s)) and (to_int[s[i+1]] > to_int[s[i]]):
                n += (to_int[s[i+1]] - to_int[s[i]])
                i += 1
            else:
                n += to_int[s[i]] 
            i += 1
        
        return n