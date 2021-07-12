class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s or len(s) == 0:
            return ""
                
        start, stop = 0, 0
        
        def expand_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            left += 1
            right -= 1
            length = right - left 
            return (length, left, right)
        
        for i in range(len(s)):
            length1, l1, r1 = expand_center(i, i)
            length2, l2, r2 = expand_center(i, i+1)
            
            max_length = max(length1, length2)
            (left, right) = (l1, r1) if length1 > length2 else (l2, r2)
            if max_length > stop - start:
                start, stop = left, right
            
        return s[start: stop+1]
                 
            
        
      