class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) == 0: 
            return 0
        elif not needle in haystack:
            return -1
        
        # this is the easy solution with python string
        # return haystack.find(needle) 
    
        # this is the manual solution
        for i,c in enumerate(haystack):
            if c == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i