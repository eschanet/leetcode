class Solution:
    
    import re
    
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^A-Za-z0-9]+', '', s)
        return s[::-1].lower() == s.lower()